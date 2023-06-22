"""Provides functions for generating code examples from a Python file."""
import os

def generate_code_examples(file_path, output_dir):
    """Generate code examples from a Python file.

    Parameters
    ----------
    file_path : str
        Path to the Python file.
    output_dir : str
        Path to the output directory.

    """
    with open(file_path, "r") as file:
        content = file.read()

    examples = content.split("# ----------------------------------------------------------------")

    script_name = os.path.splitext(os.path.basename(file_path))[0]

    for i, example in enumerate(examples):
        file_name = f"{script_name}_{i+1}.py"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as file:
            file.write(example.strip())

