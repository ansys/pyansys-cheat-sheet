import ansys.motorcad.core as pymotorcad

mcad = pymotorcad.MotorCAD()
mcad.load_from_file(r"path/motor_cad.mot")
# Load predefined template
mcad.load_template(template_name)
# saving file to working_folder
mcad.save_to_file(
    os.path.join(working_folder, mcad_name + ".mot")
)
# Exit Motor-CAD
mcad.quit()
# BREAK BLOCK

mcad.set_variable("Slot_Number", 24)
mcad.set_variable("Tooth_Width", 6)
mcad.set_variable("Magnet_Thickness", 4.5)
mcad.set_variable("Pole_Number", 4)
# BREAK BLOCK

mcad.set_variable("MagWindingType", 1)
set_variable("MagTurnsConductor", 12)
# BREAK BLOCK

mcad.set_component_material("Stator Lam (Back Iron)", "M250-35A")
mcad.set_component_material("Rotor Lam (Back Iron)", "M250-35A")
# BREAK BLOCK

# Build options
mcad.set_variable("ModelType_MotorLAB", 1)
mcad.set_variable("SatModelPoints_MotorLAB", 0)
mcad.set_variable("LossModel_Lab", 0)
mcad.set_variable("ModelBuildSpeed_MotorLAB", 10000)
mcad.set_variable("MaxModelCurrent_MotorLAB", 480)
mcad.set_variable("BuildSatModel_MotorLAB", True)

# Set lab context and build model
mcad.set_motorlab_context()
mcad.clear_model_build_lab()
mcad.build_model_lab()
# BREAK BLOCK

mcad.set_variable("OperatingMode_Lab", 0)
# setting magnetic calculation options
mcad.set_variable("EmagneticCalcType_Lab", 0)
mcad.set_variable("SpeedMax_MotorLAB", 10000)
mcad.set_variable("Speedinc_MotorLAB", 250)
mcad.set_variable("SpeedMin_MotorLAB", 500)
mcad.set_variable("Imax_MotorLAB", 480)
# BREAK BLOCK

mcad.calculate_magnetic_lab()
# BREAK BLOCK

mcad.set_variable("OpPointSpec_MotorLAB", 1)
mcad.set_variable("StatorCurrentDemand_Lab", 480)
mcad.set_variable("SpeedDemand_MotorLAB", 4000)
mcad.set_variable("LabThermalCoupling", 0)
mcad.set_variable("LabMagneticCoupling", 0)
# BREAK BLOCK

mcad.calculate_operating_point_lab()
# BREAK BLOCK

# Set the torque calculation options
points_per_cycle = 60
number_cycles = 1
mcad.set_variable("TorquePointsPerCycle", points_per_cycle)
mcad.set_variable("TorqueNumberCycles", number_cycles)
# Disable all performance tests except the ones for transient torque
mcad.set_variable("BackEMFCalculation", False)
mcad.set_variable("CoggingTorqueCalculation", False)
# Enable transient torque
mcad.set_variable("TorqueCalculation", True)
# Run Emag performance tests
mcad.do_magnetic_calculation()
# BREAK BLOCK

# Get the transient torque waveform in Emag
for n in range(points_per_cycle):
    (x, y) = mcad.get_magnetic_graph_point("TorqueVW", n)
    rotor_position.append(x)
    torque_.append(y)
# Calculate line voltage
line_voltage = mcad.get_variable("PeakLineLineVoltage")
# Retrieve lab performance curves
data = io.loadmat(
    os.path.join(
        working_folder, mcad_name, "Lab", "MotorLAB_elecdata.mat"
    )
)
speed = data["Speed"]
shaft_torque = data["Shaft_Torque"]
shaft_power = data["Shaft_Power"]
# BREAK BLOCK

pymotorcad = py.importlib.import_module("ansys.motorcad.core")
# BREAK BLOCK

import win32com.client

mcad = win32com.client.Dispatch("MotorCAD.AppAutomation")
# BREAK BLOCK

import ansys.motorcad.core as pymotorcad

mcad = pymotorcad.MotorCADCompatibility()
# BREAK BLOCK
