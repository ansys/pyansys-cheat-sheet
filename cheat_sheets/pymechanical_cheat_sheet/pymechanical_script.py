import ansys.mechanical.core as pymechanical

mechanical = pymechanical.launch_mechanical()
# BREAK BLOCK
#Launch Standalone Mechanical from Terminal : Local or Remote
"C:/Program Files/ANSYS Inc/v2xx/aisol/bin/winx64/AnsysWBU.exe" -DSApplet -AppModeMech  -nosplash -notabctrl -grpc 10000
# BREAK BLOCK
import ansys.mechanical.core as pymechanical

#Local . default port is 10000
mechanical = pymechanical.Mechanical(port= 10000)

#Remote
mechanical = pymechanical.Mechanical("192.168.0.1", port=10000)

# BREAK BLOCK
print(mechanical)
#or
print(mechanical.version)
# BREAK BLOCK
wb_exe = find_mechanical(232)[0]
# ('C:\\Program Files\\ANSYS Inc\\v232\\aisol\\bin\\winx64\\AnsysWBU.exe', 23.2)
mechanical = launch_mechanical(exec_file=wb_exe, verbose_mechanical=True, batch=True)
print(mechanical)
# BREAK BLOCK
mechanical = pymechanical.launch_mechanical(batch=False)
# BREAK BLOCK
result1 = mechanical.run_python_script("2+3")
result2 = mechanical.run_python_script("ExtAPI.DataModel.Project.ProjectDirectory")
mechanical.run_python_script("Model.AddStaticStructuralAnalysis()")
# BREAK BLOCK

# To Import a  Material
commands="""
cu_mat__file_path = r'D:\Workdir\copper.xml'.replace("\\", "\\\\")
materials = ExtAPI.DataModel.Project.Model.Materials
materials.Import(cu_mat__file_path)"""

mechanical.run_python_script(commands)
# BREAK BLOCK
mechanical.run_python_script_from_file(file_path)
# BREAK BLOCK



file =  r'D:\\Workdir\\bracket.mechdb'
command = f'ExtAPI.DataModel.Project.Open("{file}")'
mechanical.run_python_script(command)

mechanical.run_python_script("allbodies=ExtAPI.DataModel.Project.Model.GetChildren( DataModelObjectCategory.Body,True)")
mechanical.run_python_script("allbodies.Count")

# BREAK BLOCK


#Get the project directory
mechanical.project_directory

#List the files in the working directory.
mechanical.list_files()

#Save
mechanical.run_python_script("ExtAPI.DataModel.Project.Save(r'D:\\Workdir')")

#Exit 
mechanical.exit(force=True)





# BREAK BLOCK
from ansys.mechanical.core import App, global_variables
app = App(version =232)
globals().update(global_variables(app))
print(app)

# BREAK BLOCK
file =  r'D:\\Workdir\\bracket.mechdb'
app.open(file)
allbodies=ExtAPI.DataModel.Project.Model.GetChildren( Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body,True)
print(allbodies.Count)