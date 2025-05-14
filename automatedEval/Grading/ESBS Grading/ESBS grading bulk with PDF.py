# Cambiar los paths de los archivos a leer y escribir

import os
import PyPDF2
import docx
import markdown
from openai import OpenAI
from typing import Dict
import json
from Cocoa import NSOpenPanel, NSSavePanel, NSApplication


def select_folder(title="Select Folder") -> str:
    """Select a folder using a macOS-native dialog."""
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_(title)
    panel.setCanChooseFiles_(False)
    panel.setCanChooseDirectories_(True)
    panel.setAllowsMultipleSelection_(False)

    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None


class DocumentGrader:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def read_pdf(self, file_path: str) -> str:
        """Extract text from a PDF file."""
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                return "\n".join(page.extract_text() for page in pdf_reader.pages)
        except Exception as e:
            raise Exception(f"Error reading PDF {file_path}: {str(e)}")

    def read_docx(self, file_path: str) -> str:
        """Extract text from a DOCX file."""
        try:
            doc = docx.Document(file_path)
            return "\n".join(paragraph.text for paragraph in doc.paragraphs)
        except Exception as e:
            raise Exception(f"Error reading DOCX {file_path}: {str(e)}")

    def read_markdown(self, file_path: str) -> str:
        """Convert Markdown file to plain text."""
        try:
            with open(file_path, 'r', encoding='utf-8') as md_file:
                return markdown.markdown(md_file.read())
        except Exception as e:
            raise Exception(f"Error reading Markdown {file_path}: {str(e)}")

    def read_document(self, file_path: str) -> str:
        """Read text from various file formats."""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.read_pdf(file_path)
        elif ext == '.docx':
            return self.read_docx(file_path)
        elif ext in {'.md', '.markdown'}:
            return self.read_markdown(file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    def prepare_grading_prompt(self, exercise: str, rubric: str, solution: str) -> str:
        """Prepare grading prompt for OpenAI API."""
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
        """Grade a solution using OpenAI."""
        try:
            exercise = self.read_document(exercise_path)
            rubric = self.read_document(rubric_path)
            solution = self.read_document(solution_path)
            prompt = self.prepare_grading_prompt(exercise, rubric, solution)

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert grader who evaluates student solutions accurately and fairly."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                max_tokens=4000
            )

            return json.loads(response.choices[0].message.content.strip())
        except Exception as e:
            raise Exception(f"Grading failed: {str(e)}")

    def save_results(self, results: Dict, output_base_path: str):
        """Save grading results to DOCX and JSON files."""
        try:
            # Save to DOCX
            doc = docx.Document()
            doc.add_heading('Grading Results', 0)
            doc.add_heading('Analysis', level=1)
            doc.add_paragraph(results.get('analysis', 'No analysis provided'))

            doc.add_heading('Criterion Scores', level=1)
            for criterion, score in results.get('criterion_scores', {}).items():
                doc.add_paragraph(f"{criterion}: {score}")

            doc.add_heading('Total Score', level=1)
            doc.add_paragraph(str(results.get('total_score', 'No score available')))

            doc.add_heading('Feedback', level=1)
            doc.add_paragraph(results.get('feedback', 'No feedback provided'))

            doc.save(f"{output_base_path}.docx")
            print(f"Results saved to {output_base_path}.docx")

            # Save to JSON
            with open(f"{output_base_path}.json", 'w', encoding='utf-8') as json_file:
                json.dump(results, json_file, indent=4)
            print(f"Results saved to {output_base_path}.json")

        except Exception as e:
            raise Exception(f"Error saving results: {e}")


def main():
    try:
        api_key = os.getenv('MI_CLAVE_API_OPENAI')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables.")

        grader = DocumentGrader(api_key)

        exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Exercise instructions.md"
        rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Grading rubric.md"
        # solution_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam"
        # output_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam graded"
        
        print("Select the folder containing student solutions...")
        solutions_folder = select_folder("Select Folder with Student Solutions")
        if not solutions_folder:
            raise ValueError("No folder selected.")

        print("Select the folder to save grading results...")
        output_folder = select_folder("Select Folder to Save Grading Results")
        if not output_folder:
            raise ValueError("No output folder selected.")
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(solutions_folder):
            if os.path.splitext(filename)[1].lower() in {'.pdf', '.docx'}:
                solution_path = os.path.join(solutions_folder, filename)
                output_base_path = os.path.join(output_folder, f"graded_{os.path.splitext(filename)[0]}")

                print(f"Grading solution: {filename}")
                try:
                    results = grader.grade_solution(exercise_path, rubric_path, solution_path)
                    grader.save_results(results, output_base_path)
                except Exception as e:
                    print(f"Error grading {filename}: {str(e)}")

        print("Grading completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
