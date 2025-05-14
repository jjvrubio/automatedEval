
# Toma un archivo de ejercicio en PDF, un archivo de rúbrica y un archivo de solución de estudiante, y utiliza la API de OpenAI para calificar la solución del estudiante.
# Me sirve para ESBS. Hay que cambiar siempre los ficheros que describen el ejercicio y la rúbrica.
# 1. Seleccionar el archivo de solución del estudiante
# 2. Seleccionar la ubicación donde guardar los resultados de la calificación
# 3. Utiliza la API de OpenAI para calificar la solución del estudiante
# 4. Guarda los resultados de la calificación en un archivo de Word
# 5. Muestra un mensaje de error si algo sale mal

import os
import docx
from openai import OpenAI
from typing import Dict, Literal
import json
from AppKit import (NSOpenPanel, NSApplication, NSSavePanel)
import PyPDF2

FileType = Literal['.pdf', '.docx']

def select_student_file() -> str:
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Select Student's Solution File")
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["pdf"])
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

def select_save_location(suggested_filename: str) -> str:
    NSApplication.sharedApplication()
    panel = NSSavePanel.alloc().init()
    panel.setTitle_("Save Grading Results")
    panel.setNameFieldStringValue_(suggested_filename)
    panel.setAllowedFileTypes_(["docx"])
    if panel.runModal() == 1:
        return panel.URL().path()
    return None

class DocumentGrader:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def read_pdf(self, file_path: str) -> str:
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = [page.extract_text() for page in pdf_reader.pages]
                return '\n'.join(filter(None, text))
        except Exception as e:
            raise Exception(f"Error reading PDF {file_path}: {str(e)}")

    def read_docx(self, file_path: str) -> str:
        try:
            doc = docx.Document(file_path)
            return '\n'.join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
        except Exception as e:
            raise Exception(f"Error reading document {file_path}: {str(e)}")

    def read_document(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.read_pdf(file_path)
        elif ext == '.docx':
            return self.read_docx(file_path)
        else:
            raise Exception(f"Unsupported file format: {ext}")

    def prepare_grading_prompt(self, exercise: str, rubric: str, solution: str) -> str:
        return f'''Please grade the following student solution based on the exercise description and grading rubric provided.

    Exercise Description:
    {exercise}

    Grading Rubric:
    {rubric}

    Student's Solution:
    {solution}

    Please provide:
    1. A detailed analysis of the solution
    2. Points awarded for each rubric criterion
    3. Total score
    4. Specific feedback and suggestions for improvement

    Format your response ONLY as JSON with the following structure:
    {{
        "analysis": "detailed analysis here",
        "criterion_scores": {{
            "criterion1": "score",
            "criterion2": "score"
        }},
        "total_score": "numerical_score",
        "feedback": "detailed feedback here"
    }}
'''

    def grade_solution(self, exercise_path: str, rubric_path: str, solution_path: str) -> Dict:
        exercise_text = self.read_document(exercise_path)
        rubric_text = self.read_document(rubric_path)
        solution_text = self.read_document(solution_path)
        if not all([exercise_text, rubric_text, solution_text]):
            raise ValueError("One or more documents are empty")

        prompt = self.prepare_grading_prompt(exercise_text, rubric_text, solution_text)
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert grader who evaluates student solutions accurately and fairly."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=4000,
        )
        response_content = response.choices[0].message.content.strip()
        return json.loads(response_content)

    def save_results_to_docx(self, results: Dict, output_path: str):
        try:
            doc = docx.Document()
            doc.add_heading('Grading Results', 0).alignment = 1
            sections = [
                ('Analysis', 'analysis', 'No analysis provided'),
                ('Criterion Scores', 'criterion_scores', {}),
                ('Total Score', 'total_score', 'No score available'),
                ('Feedback', 'feedback', 'No feedback provided')
            ]
            for heading, key, default in sections:
                doc.add_heading(heading, level=1)
                if key == 'criterion_scores':
                    for criterion, score in results.get(key, {}).items():
                        doc.add_paragraph(f"{criterion}: {score}")
                else:
                    doc.add_paragraph(str(results.get(key, default)))
            doc.save(output_path)
            print(f"Results successfully saved to {output_path}")
        except Exception as e:
            raise Exception(f"Error saving results to DOCX: {str(e)}")

    def save_results_to_json(self, results: Dict, output_path: str):
        try:
            json_output_path = f"{os.path.splitext(output_path)[0]}.json"
            with open(json_output_path, 'w') as json_file:
                json.dump(results, json_file, indent=4)
            print(f"Results successfully saved to {json_output_path}")
        except Exception as e:
            raise Exception(f"Error saving results to JSON: {str(e)}")

def main():
    try:
        api_key = os.getenv('MI_CLAVE_API_OPENAI')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")

        grader = DocumentGrader(api_key)

        exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Exercise instructions.docx"
        rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/interview rubric.docx"
        
        print("Please select the student's solution file (PDF)...")
        solution_path = select_student_file()
        if not solution_path:
            raise ValueError("No student solution file was selected")

        solution_filename = os.path.basename(solution_path)
        suggested_output_filename = f"{os.path.splitext(solution_filename)[0]}_graded.docx"
        print("Please select where to save the grading results...")
        output_path = select_save_location(suggested_output_filename)
        if not output_path:
            raise ValueError("No save location was selected")

        results = grader.grade_solution(exercise_path, rubric_path, solution_path)
        grader.save_results_to_docx(results, output_path)
        grader.save_results_to_json(results, output_path)

        print("Grading completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
