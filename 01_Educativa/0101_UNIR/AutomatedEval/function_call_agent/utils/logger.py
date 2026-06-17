import os
import datetime


def debug_log(message: str, output_dir: str = "", title: str = "debug_log"):
    if not output_dir:
        output_dir = os.getcwd()
    debug_file = os.path.join(output_dir, f"{title}.md")
    try:
        with open(debug_file, "a") as log_file:
            timestamp = datetime.datetime.now().isoformat()
            log_file.write(f"- **[{timestamp}]** {message}\n")
    except Exception as e:
        print(f"Error al registrar log: {e}")
