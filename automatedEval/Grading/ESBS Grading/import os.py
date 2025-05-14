'''This program defines a FileReader class that handles reading and cleaning content from DOCX and PDF files. It includes methods to:
Clean and validate extracted text (clean_text).
Read content from a DOCX file (read_docx).
Read content from a PDF file (read_pdf).
Determine the file type and read the content accordingly (read_file).
The clean_text method removes non-printable characters and ensures the text is not empty. 
The read_docx and read_pdf methods extract text from DOCX and PDF files, respectively, and clean the text using clean_text. 
The read_file method determines the file extension and calls the appropriate method to read and clean the file content.
'''


import os
import docx
import PyPDF2
import openai  # OpenAI API client
from typing import Dict, Any
import json
import time

class FileReader:
    """Handles reading and cleaning of file content."""

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and validate extracted text."""
        if not text.strip():
            raise ValueError("Extracted text is empty.")
        return ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t').strip()

    @staticmethod
    def read_docx(file_path: str) -> str:
        """Read content from a DOCX file."""
        try:
            doc = docx.Document(file_path)
            return FileReader.clean_text('\n'.join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()))
        except Exception as e:
            raise Exception(f"Error reading DOCX file {file_path}: {str(e)}")

    @staticmethod
    def read_pdf(file_path: str) -> str:
        """Read content from a PDF file."""
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = []
                for page in pdf_reader.pages:
                    text.append(page.extract_text())
                return FileReader.clean_text('\n'.join(text))
        except Exception as e:
            raise Exception(f"Error reading PDF file {file_path}: {str(e)}")

    @staticmethod
    def read_file(file_path: str) -> str:
        """Read and clean content from various file types."""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.docx':
            return FileReader.read_docx(file_path)
        elif ext == '.pdf':
            return FileReader.read_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")


class OpenAIClient:
    """Handles communication with the OpenAI API."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_base = "https://api.openai.com/v1"

    def get_completion(self, prompt: str, model: str = "gpt-4", max_tokens: int = 4000, temperature: float = 0.0) -> str:
        """
        Fetch completion from OpenAI Chat Completions API.
        """
        import requests  # Using requests to make HTTP calls
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            response = requests.post(f"{self.api_base}/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            response_data = response.json()
            if "choices" in response_data and len(response_data["choices"]) > 0:
                return response_data["choices"][0]["message"]["content"].strip()
            else:
                raise ValueError("Unexpected response structure from OpenAI API.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with OpenAI API: {e}")


class DocumentGrader:
    """Class for grading student solutions using OpenAI API."""

    def __init__(self, api_client, file_reader):
        self.api_client = api_client
        self.file_reader = file_reader

    def prepare_grading_prompt(self, exercise: str, rubric: str, solution: str) -> str:
        """Prepare the grading prompt for the API."""
        def clean_input(text):
            return text.replace('"', '\\"').replace('\n', ' ').replace('\r', '').strip()

        exercise = clean_input(exercise)
        rubric = clean_input(rubric)
        solution = clean_input(solution)

        return f"""
Human: Please grade the following student solution based on the exercise description and grading rubric provided.

Exercise Description:
{exercise}

Grading Rubric:
{rubric}

Student's Solution:
{solution}

Please provide your response in valid JSON format:
{{
    "analysis": "Your analysis here",
    "criterion_scores": {{
        "criterion1": "score",
        "criterion2": "score"
    }},
    "total_score": "final_score",
    "feedback": "Your feedback here"
}}

Assistant:"""

    def grade_solution(self, exercise_path: str, rubric_path: str, solution_path: str) -> Dict:
        """Grade the solution using OpenAI API."""
        try:
            # Prepare the grading prompt
            exercise_text = self.file_reader.read_file(exercise_path)
            rubric_text = self.file_reader.read_file(rubric_path)
            solution_text = self.file_reader.read_file(solution_path)

            prompt = self.prepare_grading_prompt(exercise_text, rubric_text, solution_text)

            # Fetch the response from the API
            raw_response = self.api_client.get_completion(prompt, model="gpt-4")

            # Parse the JSON response
            return self.sanitize_and_fallback_results(raw_response)

        except Exception as e:
            return {
                "analysis": "Error: Grading failed",
                "criterion_scores": {},
                "total_score": 0,
                "feedback": f"Error details: {e}"
            }

    def sanitize_and_fallback_results(self, raw_response: str) -> Dict:
        """
        Sanitize and fallback mechanism for JSON response.
        If JSON parsing fails, return a fallback structure.
        """
        try:
            parsed_results = json.loads(raw_response)
            return parsed_results
        except json.JSONDecodeError as e:
            return {
                "analysis": "Error: Could not parse response",
                "criterion_scores": {},
                "total_score": 0,
                "feedback": f"Error processing response: {e}. Original response: {raw_response[:500]}..."
            }

    def save_results_to_docx(self, results: Dict, docx_path: str):
        """Save grading results to a DOCX file."""
        try:
            doc = docx.Document()
            doc.add_heading('Grading Results', 0)

            # Add sections for analysis, criterion scores, total score, and feedback
            doc.add_heading('Analysis', level=1)
            doc.add_paragraph(results.get('analysis', 'No analysis provided'))

            doc.add_heading('Criterion Scores', level=1)
            for criterion, score in results.get('criterion_scores', {}).items():
                doc.add_paragraph(f"{criterion}: {score}")

            doc.add_heading('Total Score', level=1)
            doc.add_paragraph(str(results.get('total_score', 'No score available')))

            doc.add_heading('Feedback', level=1)
            doc.add_paragraph(results.get('feedback', 'No feedback provided'))

            doc.save(docx_path)
        except Exception as e:
            raise Exception(f"Error saving results to DOCX for {docx_path}: {e}")

    def save_results(self, results: Dict, solution_path: str, output_dir: str):
        """Save grading results to JSON and DOCX files."""
        base_name = os.path.splitext(os.path.basename(solution_path))[0]
        json_output_path = os.path.join(output_dir, f"{base_name}_graded.json")
        docx_output_path = os.path.join(output_dir, f"{base_name}_graded.docx")

        # Save JSON
        with open(json_output_path, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, indent=4)

        # Save DOCX
        self.save_results_to_docx(results, docx_output_path)


def main():
    # Paths for exercise, rubric, solutions directory, and output directory
    exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Exercise instructions.docx"
    rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/interview rubric.docx"
    solutions_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam/"
    output_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam graded/"

    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables.")

    grader = DocumentGrader(
        api_client=OpenAIClient(api_key),
        file_reader=FileReader()
    )

    # Process each solution file
    for solution_file in os.listdir(solutions_dir):
        solution_path = os.path.join(solutions_dir, solution_file)

        # Check if the file is supported
        if not solution_file.lower().endswith(('.docx', '.pdf')):
            continue

        try:
            results = grader.grade_solution(exercise_path, rubric_path, solution_path)
            grader.save_results(results, solution_path, output_dir)
        except Exception as e:
            print(f"Error grading {solution_file}: {e}")


if __name__ == "__main__":
    main()
