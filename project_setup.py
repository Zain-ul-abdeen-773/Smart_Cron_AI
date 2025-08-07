import os

# Define project structure
project_structure = {
    "smartcronai": {
        "app": {
            "__init__.py": "",
            "routes.py": "",
            "ai_parser.py": "",
            "scheduler.py": "",
            "utils.py": "",
            "models": {
                "__init__.py": "",
                "sql_models.py": "",
                "nosql_models.py": ""
            },
            "templates": {
                "base.html": "",
                "dashboard.html": "",
                "new_task.html": ""
            },
            "static": {
                "css": {
                    "style.css": ""
                },
                "js": {
                    "main.js": ""
                },
                "icons": {}
            }
        },
        "tasks": {
            "jobs.py": "",
            "monitor.py": ""
        },
        "migrations": {},
        "instance": {
            "config.py": ""
        },
        "requirements.txt": "",
        "Dockerfile": "",
        "celery_worker.py": "",
        "run.py": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Create the project structure
base_path = "/mnt/data"
create_structure(base_path, project_structure)

"✅ Project structure for 'SmartCronAI' created."
