import ansys.fluent.core as pyfluent

solver = pyfluent.launch_fluent(mode="solver", show_gui=True)
# BREAK BLOCK
mesh_filename = "example_file.msh.h5"
solver.file.read(file_type="mesh", file_name=mesh_filename)
# BREAK BLOCK

# e.g., read_case(), read_case_data()
case_filename = "example_file.cas.h5"
solver.file.read_case(file_type="case", file_name=case_filename)
# BREAK BLOCK

solver.setup.models.energy.enabled = True
# BREAK BLOCK

# >>> from pprint import pprint
# >>> pprint(solver.setup.models.energy())
{
    "enabled": True,
    "inlet_diffusion": True,
    "kinetic_energy": False,
    "pressure_work": False,
    "viscous_dissipation": False,
}
# BREAK BLOCK

solver.setup.materials.copy_database_material_by_name(
    type="fluid", name="water-liquid"
)
solver.setup.cell_zone_conditions.fluid[
    "elbow-fluid"
].material = "water-liquid"
# BREAK BLOCK

solver.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].vmag = {
    "option": "constant or expression",
    "constant": 0.4,
}
solver.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].ke_spec = "Intensity and Hydraulic Diameter"
solver.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].turb_intensity = 5
solver.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].turb_hydraulic_diam = "4 [in]"
solver.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].t = {
    "option": "constant or expression",
    "constant": 293.15,
}
# BREAK BLOCK
solver.setup.cell_zone_conditions.fluid["elbow-fluid"] = {
    "laminar": True
}
# BREAK BLOCK
solver.solution.initialization.hybrid_initialize()
solver.solution.run_calculation.iterate(number_of_iterations=150)
# BREAK BLOCK
solver.results.graphics.contour["contour"] = {}
solver.results.graphics.contour["contour"].print_state()
solver.results.graphics.contour["contour"].field = "temperature"
solver.results.graphics.contour["contour"].surfaces_list = [
    "symmetry-xyplane"
]
