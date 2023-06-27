import os
import argparse

THIS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(THIS_PATH, "generated_scripts")

def generate_code_examples(file_path):
    """Generate code examples from a Python file.

    Parameters
    ----------
    file_path : str
        Path to the Python file.

    """
    with open(file_path, "r") as file:
        content = file.read()

    examples = content.split("# BREAK BLOCK")

    script_name = os.path.splitext(os.path.basename(file_path))[0]

    for i, example in enumerate(examples):
        file_name = f"{script_name}_{i}.py"
        file_path = os.path.join(OUTPUT_PATH, file_name)
        with open(file_path, "w") as file:
            file.write(example.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code examples from a Python file.")
    parser.add_argument("file_path", help="Path to the Python file.")
    args = parser.parse_args()

    generate_code_examples(args.file_path)
