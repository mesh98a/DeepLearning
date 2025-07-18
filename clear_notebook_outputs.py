import os
from nbformat import read, write, NO_CONVERT
from nbconvert.preprocessors import ClearOutputPreprocessor

def clear_outputs_in_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = read(f, as_version=NO_CONVERT)

    preprocessor = ClearOutputPreprocessor()
    preprocessor.preprocess(nb, {})

    with open(notebook_path, "w", encoding="utf-8") as f:
        write(nb, f)

def clear_all_notebooks_outputs(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".ipynb") and not file.startswith("."):
                full_path = os.path.join(root, file)
                print(f"Clearing outputs: {full_path}")
                clear_outputs_in_notebook(full_path)

if __name__ == "__main__":
    clear_all_notebooks_outputs(".")  # Aktuelles Verzeichnis
