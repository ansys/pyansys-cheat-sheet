import ansys.mechanical.core as pymechanical

mechanical = pymechanical.launch_mechanical()
# BREAK BLOCK
# Standalone Mechanical from a local or remote terminal
ansys-mechanical -r 241 --port 10000 -g
# BREAK BLOCK
import ansys.mechanical.core as pymechanical
# #Note: The following code uses port 10000, but you can specify an alternative port if required.

# Either connect locally
mechanical = pymechanical.Mechanical(port=10000)

# Or connect remotely, specifying the IP address or hostname and port.
mechanical = pymechanical.Mechanical("192.168.0.1", port=10000)

# BREAK BLOCK
print(mechanical)

# BREAK BLOCK
from ansys.mechanical.core import find_mechanical

wb_exe = find_mechanical(241)[0]
# 'Ansys Inc\\v241\\aisol\\bin\\winx64\\AnsysWBU.exe'
mechanical = launch_mechanical(
    exec_file=wb_exe, verbose_mechanical=True, batch=True)
print(mechanical)
# BREAK BLOCK
mechanical = pymechanical.launch_mechanical(batch=False)
# BREAK BLOCK
result1 = mechanical.run_python_script("2+3")
result2 = mechanical.run_python_script(
    "ExtAPI.DataModel.Project.ProjectDirectory"
)
mechanical.run_python_script(
    "Model.AddStaticStructuralAnalysis()"
)
# BREAK BLOCK
# Import a  material
commands = """
cu_mat__file_path = r'D:\Workdir\copper.xml'.replace("\\", "\\\\")
materials = ExtAPI.DataModel.Project.Model.Materials
materials.Import(cu_mat__file_path)"""
mechanical.run_python_script(commands)
# BREAK BLOCK
mechanical.run_python_script_from_file(file_path)
# BREAK BLOCK
file = r"D:\\Workdir\\bracket.mechdb"
command = f'ExtAPI.DataModel.Project.Open("{file}")'
mechanical.run_python_script(command)
mechanical.run_python_script(
    "allbodies=ExtAPI.DataModel.Project.Model.GetChildren( DataModelObjectCategory.Body,True)")
mechanical.run_python_script("allbodies.Count")
# BREAK BLOCK
# Get the project directory
mechanical.project_directory

# List the files in the working directory.
mechanical.list_files()
# Save
mechanical.run_python_script(
    "ExtAPI.DataModel.Project.Save(r'D:\\Workdir')")
# Log in two ways:
mechanical._log.info("This is a useful message.")
mechanical.log_message("INFO", "info message")
# Exit
mechanical.exit(force=True)


# BREAK BLOCK
from ansys.mechanical.core import App

app = App(version=241)
print(app)
# BREAK BLOCK

# Extract the global API entry points (available from built-in Mechanical scripting)
# Merge them into your Python global variables
app.update_globals(globals())
# BREAK BLOCK
ExtAPI  # Application.ExtAPI
DataModel  # Application.DataModel
Model  # Application.DataModel.Project.Model
Tree  # Application.DataModel.Tree
Graphics  # Application.ExtAPI.Graphics

# BREAK BLOCK
file = r"D:\\Workdir\\bracket.mechdb"
app.open(file)
allbodies = DataModel.Project.Model.GetChildren(
    Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body,
    True)
print(allbodies.Count)
# BREAK BLOCK
import logging
from ansys.mechanical.core import App
from ansys.mechanical.core.embedding.logger import (
    Configuration,
    Logger)

Configuration.configure(level=logging.WARNING, to_stdout=True)
app = App(version=241)
Logger.error("message")