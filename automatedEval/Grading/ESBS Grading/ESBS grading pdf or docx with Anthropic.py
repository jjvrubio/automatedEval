import os
import docx
import PyPDF2
import anthropic
from typing import Dict, Any
import json
import time
import logging

# Configure logging
logging.basicConfig(
    filename='grading_debug.log',  # Log file name
    filemode='w',                 # Append mode (use 'a' to update on each run)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG            # Set the logging level to DEBUG
)

logging.info("Logging initialized. Starting script...")


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


class AnthropicClient:
    """Handles communication with the Anthropic API."""

    def __init__(self, api_key: str):
        try:
            logging.info("Initializing Anthropic client.")
            self.client = anthropic.Client(api_key=api_key)
        except Exception as e:
            raise Exception(f"Error initializing Anthropic client: {str(e)}")

    def get_completion(self, prompt: str, model: str, max_tokens: int = 4000, temperature: float = 0.0) -> str:
        """Fetch completion from Anthropic Messages API."""
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )
            if isinstance(response, dict):
                # Serialize dict to JSON string for consistency
                return json.dumps(response)
            elif isinstance(response, str):
                # Return string directly if already in expected format
                return response
            else:
                raise ValueError("Unexpected API response format.")
        except Exception as e:
            raise Exception(f"Error fetching completion from API: {e}")




class DocumentGrader:
    """Class for grading student solutions using Anthropic API."""

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

        return f"""\n\nHuman: Please grade the following student solution based on the exercise description and grading rubric provided.

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
\n\nAssistant:"""

    def grade_solution(self, exercise_path: str, rubric_path: str, solution_path: str) -> Dict:
        """Grade the solution using Anthropic API."""
        try:
            exercise_text = self.file_reader.read_file(exercise_path)
            rubric_text = self.file_reader.read_file(rubric_path)
            solution_text = self.file_reader.read_file(solution_path)

            prompt = self.prepare_grading_prompt(exercise_text, rubric_text, solution_text)

            # Fetch the response from the API
            raw_response = self.api_client.get_completion(prompt, model="claude-3-haiku-20240307")

            # Sanitize the response text and parse results
            sanitized_text = self.sanitize_response_text(raw_response)
            return self.sanitize_and_fallback_results(sanitized_text)

        except Exception as e:
            return {
                "analysis": "Error: Grading failed",
                "criterion_scores": {},
                "total_score": 0,
                "feedback": f"Error details: {e}"
            }



    def sanitize_and_fallback_results(self, raw_response: Any) -> Dict:
        """
        Sanitize and fallback mechanism for JSON response.
        If JSON parsing fails, return a fallback structure.
        """
        try:
            # Handle case where response is already a dictionary
            if isinstance(raw_response, dict):
                return raw_response

            # Attempt to parse raw_response if it's a string
            parsed_results = json.loads(raw_response)
            return parsed_results
        except json.JSONDecodeError as e:
            return {
                "analysis": "Error: Could not parse response",
                "criterion_scores": {},
                "total_score": 0,
                "feedback": f"Error processing response: {e}. Original response: {str(raw_response)[:500]}..."
            }




    def sanitize_response_text(self, response_text: str) -> str:
        """Sanitize raw response text by removing invalid characters."""
        # Allow printable characters and common escape sequences
        sanitized_text = ''.join(char for char in response_text if ord(char) >= 32 or char in '\n\r\t').strip()
        # logging.debug(f"Sanitized response text: {sanitized_text[:500]}...")
        return sanitized_text


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
            logging.info(f"Results saved to DOCX: {docx_path}")

        except Exception as e:
            logging.error(f"Error saving results to DOCX for {docx_path}: {e}")



    def save_results(self, results: Dict, solution_path: str, output_dir: str):
        
        
        # Log paths
        # logging.info(f"Saving JSON to: {json_output_path}")
        # logging.info(f"Saving DOCX to: {docx_output_path}"))

        try:
            # Generate unique output file paths
            base_name = os.path.splitext(os.path.basename(solution_path))[0]
            json_output_path = os.path.join(output_dir, f"{base_name}_graded.json")
            docx_output_path = os.path.join(output_dir, f"{base_name}_graded.docx")


            # Save JSON
            sanitized_results = self.sanitize_and_fallback_results(results)
            with open(json_output_path, 'w', encoding='utf-8') as json_file:
                json.dump(sanitized_results, json_file, indent=4)
            # logging.info(f"Results saved to JSON: {json_output_path}")

            # Save DOCX
            self.save_results_to_docx(sanitized_results, docx_output_path)

        except Exception as e:
            logging.error(f"Error saving results for {solution_path}: {e}")



def main():
    logging.info("Script execution started.")

    try:
        # Initialize the grader with the Anthropic API key
        api_key = os.getenv("MI_CLAVE_API_ANTHROPIC")
        if not api_key:
            raise ValueError("Anthropic API key not found in environment variables.")
        grader = DocumentGrader(
            api_client=AnthropicClient(api_key),
            file_reader=FileReader()
        )
    except Exception as e:
        logging.error(f"Error initializing DocumentGrader: {e}")
        return

    # Paths for exercise, rubric, solutions directory, and output directory
    exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Exercise instructions.docx"
    rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/interview rubric.docx"
    solutions_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam/"
    output_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam graded/"

    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    # Process each solution file
    for solution_file in os.listdir(solutions_dir):
        solution_path = os.path.join(solutions_dir, solution_file)
        
        # Check if the file is supported
        if not solution_file.lower().endswith(('.docx', '.pdf')):
            logging.warning(f"Skipping unsupported file: {solution_file}")
            continue

        try:
            logging.info(f"Processing file: {solution_file}")
            results = grader.grade_solution(exercise_path, rubric_path, solution_path)

            # Save results to the output directory
            grader.save_results(results, solution_path, output_dir)
        except Exception as e:
            logging.error(f"Error grading {solution_file}: {e}")

    logging.info("Grading completed successfully.")


if __name__ == "__main__":
    main()
