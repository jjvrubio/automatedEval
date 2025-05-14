import os
import docx
import anthropic
from typing import Dict
import json


class DocumentGrader:
    def __init__(self, api_key: str):
        """Initialize the grader with Anthropic API key."""
        try:
            print(f"Initializing Anthropic client with API key: {api_key}")
            self.client = anthropic.Client(api_key=api_key)
        except Exception as e:
            raise Exception(f"Error initializing Anthropic client: {str(e)}")

    def read_docx(self, file_path: str) -> str:
        """Read content from a Word document."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            doc = docx.Document(file_path)
            return '\n'.join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
        except Exception as e:
            raise Exception(f"Error reading document {file_path}: {str(e)}")

    def prepare_grading_prompt(self, exercise: str, rubric: str, solution: str) -> str:
        """Prepare the prompt for Anthropic API."""
        prompt_content = f"""Please grade the following student solution based on the exercise description and grading rubric provided.

        Exercise Description:
        {exercise}

        Grading Rubric:
        {rubric}

        Student's Solution:
        {solution}

        Please provide your response in valid JSON format with the following structure, ensuring no special characters or line breaks within the JSON values:
        {{
            "analysis": "Your detailed analysis in a single line",
            "criterion_scores": {{
                "criterion1": "score",
                "criterion2": "score"
            }},
            "total_score": "final_score",
            "feedback": "Your detailed feedback in a single line"
        }}

        Important: Ensure all text values are properly escaped and contain no line breaks or special characters that would make the JSON invalid.
        """
        return prompt_content



    def grade_solution(self, exercise_path: str, rubric_path: str, solution_path: str) -> Dict:
        """Grade the solution using Anthropic API."""
        try:
            # Read documents
            exercise_text = self.read_docx(exercise_path)
            rubric_text = self.read_docx(rubric_path)
            solution_text = self.read_docx(solution_path)

            # Prepare the grading prompt
            prompt = self.prepare_grading_prompt(exercise_text, rubric_text, solution_text)
            print("Sending prompt to Anthropic API...")
            print(f"Prompt:\n{prompt}")

            # Call the Anthropic API
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=4000,
                temperature=0.0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            print("API response received.")
            print(response)

            # Parse the response
            if not response.content:
                raise Exception("API response missing content.")
                
            # Clean the response text before parsing JSON
            response_text = response.content[0].text
            # Remove any control characters
            response_text = ''.join(char for char in response_text if ord(char) >= 32 or char in '\n\r\t')
            
            try:
                return json.loads(response_text)
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON response: {response_text}")
                print(f"JSON error: {str(e)}")
                # Attempt to clean and format the response
                cleaned_response = {
                    "analysis": "Error: Could not parse response",
                    "criterion_scores": {},
                    "total_score": 0,
                    "feedback": f"Error processing response: {str(e)}\nOriginal response: {response_text}"
                }
                return cleaned_response
            
        except Exception as e:
            raise Exception(f"Grading failed: {str(e)}")


    def save_results_to_json(self, results: Dict, output_path: str):
        """Save grading results to a JSON file."""
        try:
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump(results, json_file, indent=4)
            print(f"Results saved to {output_path}")
        except Exception as e:
            raise Exception(f"Error saving results to JSON: {str(e)}")



def main():
    try:
        api_key = os.getenv("MI_CLAVE_API_ANTHROPIC")
        if not api_key:
            raise ValueError("Anthropic API key not found in environment variables.")

        grader = DocumentGrader(api_key)

        exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Exercise instructions.docx"
        rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/interview rubric.docx"
        solutions_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam/"
        output_dir = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Consumer Market Research/Exercises/5th day interview/Class exam graded/"

        # Check paths
        for path, description in [
            (exercise_path, "Exercise file"),
            (rubric_path, "Rubric file"),
            (solutions_dir, "Solutions directory"),
        ]:
            if not os.path.exists(path):
                raise FileNotFoundError(f"{description} not found at: {path}")

        os.makedirs(output_dir, exist_ok=True)

        # Process each solution file
        for solution_file in os.listdir(solutions_dir):
            if not solution_file.endswith(".docx"):
                print(f"Skipping unsupported file: {solution_file}")
                continue

            solution_path = os.path.join(solutions_dir, solution_file)
            output_path = os.path.join(output_dir, f"{os.path.splitext(solution_file)[0]}_graded.json")

            print(f"Grading solution: {solution_file}")
            try:
                results = grader.grade_solution(exercise_path, rubric_path, solution_path)
                grader.save_results_to_json(results, output_path)
            except Exception as e:
                print(f"Error grading {solution_file}: {str(e)}")

        print("Grading completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
