# Toma un archivo de ejercicio en PDF, un archivo de rúbrica y un archivo de solución de estudiante, y utiliza la API de OpenAI para calificar la solución del estudiante.
# Me sirve para ESBS. Hay que cambiar siempre los ficheros que describen el ejercicio y la rúbrica.
# 1. Seleccionar el archivo de solución del estudiante
# 2. Seleccionar la ubicación donde guardar los resultados de la calificación
# 3. Utiliza la API de OpenAI para calificar la solución del estudiante
# 4. Guarda los resultados de la calificación en un archivo de Word
# 5. Muestra un mensaje de error si algo sale mal

import os
import docx
from typing import Dict, Literal
import json
from AppKit import (NSOpenPanel, NSApplication, NSSavePanel)
import PyPDF2
import sys
import logging
import anthropic

FileType = Literal['.pdf', '.docx']

# Configuración de logging a archivo y consola
LOG_PATH = os.path.join(os.path.dirname(__file__), 'grading_debug.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_PATH, mode='a', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

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
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-opus-20240229"
        self.token_limit = 200000  # Claude 3 Opus permite hasta 200k tokens

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

    def read_md(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"Error reading markdown file {file_path}: {str(e)}")

    def read_document(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.read_pdf(file_path)
        elif ext == '.docx':
            return self.read_docx(file_path)
        elif ext == '.md':
            return self.read_md(file_path)
        else:
            raise Exception(f"Unsupported file format: {ext}")

    def prepare_grading_prompt(self, exercise: str, rubric: str, solution: str) -> str:
        return f'''You are an academic evaluator applying a rigorous ultra-strict protocol.

    Exercise Description:
    {exercise}

    Grading Rubric:
    {rubric}

    Student's Solution:
    {solution}

    You will perform:
    1. A global structural and argumentative coherence analysis: identify inconsistencies between diagnosis, objectives, methodology, proposal, and results. Detect disconnections between value proposition and strategy, channels or finance.
    2. A criterion-by-criterion evaluation with extended justifications, using concrete examples from the text, and applying level-2 penalty rules when appropriate. Do not give level 4 unless the criterion is flawless.
    3. A markdown report with:
        - A section per criterion
        - Areas for improvement (unless level 4)
        - A summary table
        - A critical final conclusion
        - Three structured clarifying questions for the author

    You must also verify that the student followed the formal academic structure and expectations defined in the institutional TFM guidelines:
    - Inclusion of a title page, numbered index, executive summary, CANVA matrix
    - Logical flow: introduction → diagnosis → strategic analysis → proposal → finance → conclusions
    - Each table/figure must be titled, referenced in-text and sourced if not original
    - Citations and bibliography must follow either APA 7, Harvard, or Chicago formats without mixing
    - The proposal must derive from the diagnosis and analysis (AS-IS to TO-BE logic)

    Also, extract a separate JSON with the following structure:

    ```json
    {{
    "criterion_scores": {{
        "Criterion 1": 3,
        "Criterion 2": 2
    }},
    "total_score": 24,
    "feedback": "Full structured evaluation report."
    }}
    '''

    def count_tokens(self, *args) -> int:
        # Claude usa tokens similares a OpenAI, pero puedes usar tiktoken o simplemente len(text.split()) como aproximación
        total = 0
        for text in args:
            if text:
                total += len(text.split())  # Aproximación rápida
        return total

    def grade_solution(self, exercise_path: str, rubric_path: str, solution_path: str) -> dict:
        exercise_text = self.read_document(exercise_path)
        rubric_text = self.read_document(rubric_path)
        solution_text = self.read_document(solution_path)
        if not all([exercise_text, rubric_text, solution_text]):
            raise ValueError("One or more documents are empty")

        prompt = self.prepare_grading_prompt(exercise_text, rubric_text, solution_text)
        input_tokens = self.count_tokens(prompt)
        max_output_tokens = 4000
        total_tokens = input_tokens + max_output_tokens
        logger.info(f"[Token count] Input: {input_tokens}, Output (max): {max_output_tokens}, Total: {total_tokens}")
        if total_tokens > self.token_limit:
            logger.error(f"El total de tokens ({total_tokens}) supera el límite de {self.token_limit} para Claude 3 Opus.")
            raise ValueError(f"El total de tokens ({total_tokens}) supera el límite de {self.token_limit} para Claude 3 Opus.")

        # Claude 3 Opus API call
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_output_tokens,
            temperature=0.0,
            system="You are an expert grader who evaluates student solutions accurately and fairly.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        response_content = response.content[0].text.strip() if hasattr(response.content[0], 'text') else response.content[0]['text'].strip()
        logger.debug(f"Response content: {response_content}")

        md_output_path = os.path.splitext(solution_path)[0] + "_grading_raw.md"
        try:
            with open(md_output_path, "w", encoding="utf-8") as f:
                f.write(response_content)
            logger.info(f"Raw model output saved to {md_output_path}")
            self.process_markdown_output(md_output_path)
        except Exception as e:
            logger.error(f"Could not save raw model output to .md: {e}")

        return {"md_report": md_output_path, "json_grades": os.path.splitext(md_output_path)[0] + ".json"}


    def process_markdown_output(self, md_path: str):
        """
        Procesa el archivo .md generado por el modelo:
        - Extrae el bloque JSON (notas) y lo guarda como .json
        - El resto del markdown se puede guardar como informe organizado (ya está en el .md)
        """
        import re
        import json
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r"```(?:json|markdown)?\\s*({[\\s\\S]*?})\\s*```", content, re.DOTALL)
        json_str = None
        if match:
            json_str = match.group(1)
        else:
            match2 = re.search(r'({[\s\S]*})', content)
            if match2:
                json_str = match2.group(1)
        if json_str:
            try:
                table = json.loads(json_str)
                json_path = os.path.splitext(md_path)[0] + '.json'
                with open(json_path, 'w', encoding='utf-8') as jf:
                    json.dump(table, jf, indent=4, ensure_ascii=False)
                logger.info(f"Notas extraídas y guardadas en {json_path}")
            except Exception as e:
                logger.error(f"Error al decodificar el bloque JSON del markdown: {e}")
        else:
            logger.error(f"No se encontró bloque JSON en el markdown para {md_path}")

def pedir_api_key_dialogo() -> str:
    import subprocess
    script = 'display dialog "Introduce tu clave API de OpenAI:" default answer "" with hidden answer'
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    for line in result.stdout.split(','):
        if 'text returned:' in line:
            return line.split(':', 1)[1].strip()
    return None

def main():
    try:
        logger.info("Script iniciado.")
        api_key = os.getenv('MI_CLAVE_API_OPENAI')
        logger.info(f"API key encontrada en entorno: {bool(api_key)}")
        if not api_key:
            logger.info("No hay API key en entorno, pidiendo por diálogo...")
            api_key = pedir_api_key_dialogo()
        if not api_key:
            logger.error("No se obtuvo API key ni por entorno ni por diálogo.")
            raise ValueError("OpenAI API key not found in environment variables or user input")

        logger.info("Inicializando DocumentGrader...")
        grader = DocumentGrader(api_key)

        exercise_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Plagiarism & AI/Exercise/plagiarism Exercise instructions.md"
        rubric_path = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/ESBS/Asignaturas/Plagiarism & AI/Exercise/Plagiarism rubric.md"
        
        logger.info("Please select the student's solution file (PDF)...")
        solution_path = select_student_file()
        if not solution_path:
            logger.error("No student solution file was selected")
            raise ValueError("No student solution file was selected")

        solution_filename = os.path.basename(solution_path)
        suggested_output_filename = f"{os.path.splitext(solution_filename)[0]}_graded.docx"
        logger.info("Please select where to save the grading results...")
        output_path = select_save_location(suggested_output_filename)
        if not output_path:
            logger.error("No save location was selected")
            raise ValueError("No save location was selected")

        logger.info("Llamando a grade_solution...")
        results = grader.grade_solution(exercise_path, rubric_path, solution_path)
        logger.info("Guardando resultados...")
        # Eliminado: ya no se genera el archivo .docx ni el segundo .json

        logger.info("Grading completed successfully.")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()