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

    Returns
    -------
    List of code example files generated from the Python file.
    """
    with open(file_path, "r") as file:
        content = file.read()

    examples = content.split("# ----------------------------------------------------------------")

    for i, example in enumerate(examples):
        file_name = f"code_example_{i+1}.py"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as file:
            file.write(example.strip())

