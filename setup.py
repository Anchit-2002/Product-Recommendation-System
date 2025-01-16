import os
import subprocess

def create_project(project_name, folder_structure, venv_name='venv'):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)
    print(f"Project '{project_name}' created.")

    # Create subfolders
    for folder in folder_structure:
        path = os.path.join(project_name, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Folder '{path}' created.")

    # Create basic files
    create_file(os.path.join(project_name, 'README.md'), f"# {project_name}\n\nProject description.")
    create_file(os.path.join(project_name, '.gitignore'), "*.pyc\n__pycache__/\n.env\n")

    # Create a Python virtual environment
    create_virtualenv(os.path.join(project_name, venv_name))

    # Open the project in VS Code
    open_in_vscode(project_name)

def create_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"File '{filepath}' created.")

def create_virtualenv(venv_path):
    try:
        subprocess.run(['python', '-m', 'venv', venv_path], check=True)
        print(f"Virtual environment created at '{venv_path}'.")
    except subprocess.CalledProcessError as e:
        print("Error creating virtual environment:", e)

def open_in_vscode(project_path):
    try:
        subprocess.run(['code', project_path], check=True)
        print(f"VS Code opened for project '{project_path}'.")
    except FileNotFoundError:
        print("VS Code is not installed or not found in PATH.")

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    folder_structure = ['src', 'tests', 'docs', 'data']
    create_project(project_name, folder_structure)
