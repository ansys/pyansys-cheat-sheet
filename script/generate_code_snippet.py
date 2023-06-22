
import os
def generate_code_examples(file_path, output_dir):
    # write a docstring using google style docstring
    """Generate code examples from a python file.

    Args:
        file_path (str): Path to the python file.
        output_dir (str): Path to the output directory.

    Returns:
        List of code examples files generated given the python file.        
    """
    # read the file content

    with open(file_path, "r") as f:
        content = f.read()
    # following seperator is used to seperate the code examples. 
    # It can be any string based on the input file.
    examples = content.split(
        "# ----------------------------------------------------------------"
    )
    for i, example in enumerate(examples):
        file_name = f"code_example_{i+1}.py"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as f:
            f.write(example.strip())

# Usage e.g.:
generate_code_examples(file_path="cheat_sheets\pyfluent_cheat_sheet\pyfluent_script.py", 
                       output_dir="cheat_sheets\pyfluent_cheat_sheet")