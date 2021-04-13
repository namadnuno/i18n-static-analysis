from src.runner import run
import os

def start():
    path = os.getenv('PROJECT_PATH')
    default_namespace = os.getenv('DEFAULT_NAMESPACE')
    report_path = os.getenv('REPORT_FILE_PATH')
    run(path, { 'default_namespace': default_namespace, 'report_path': report_path })