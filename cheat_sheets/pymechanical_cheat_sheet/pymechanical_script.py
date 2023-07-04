import ansys.mechanical.core as pymechanical

mechanical = pymechanical.launch_mechanical()
# BREAK BLOCK
"C:/Program Files/ANSYS Inc/v2xx/aisol/bin/winx64/AnsysWBU.exe" -DSApplet -AppModeMech  -nosplash -notabctrl -grpc 10000
# BREAK BLOCK

import ansys.mechanical.core as pymechanical

mechanical = pymechanical.Mechanical(port= 10000) # default port is 10000
# BREAK BLOCK
"C:/Program Files/ANSYS Inc/v2xx/aisol/bin/winx64/AnsysWBU.exe" -DSApplet -AppModeMech  -nosplash -notabctrl -grpc 10000

# BREAK BLOCK
import ansys.mechanical.core as pymechanical

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

