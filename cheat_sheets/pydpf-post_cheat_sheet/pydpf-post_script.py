from ansys.dpf import post
from ansys.dpf.post import examples

sim = post.load_simulation(r"C:\Users\user\file.rst")
# BREAK BLOCK

sim = post.load_simulation(r"/home/user/file.rst")
# BREAK BLOCK

example_path = examples.find_static_rst()
simulation = post.load_simulation(example_path)
print(simulation)
# BREAK BLOCK

mesh = simulation.mesh
print(mesh)
# BREAK BLOCK

disp = simulation.displacement()
x_disp = simulation.displacement(components=["X"])
# Extract displacement on specific nodes from already extracted large data set
nodes_disp = disp.select(node_ids=[1, 10, 100])
# Extract displacement on specific nodes from result file
nodes_disp = simulation.displacement(node_ids=[1, 10, 100])
# BREAK BLOCK

elem_nodal_stress = simulation.stress()
nodal_stress = simulation.stress_nodal()
elemental_stress = simulation.stress_elemental()
# Extract elemental stresses on specific elements
elemental_stress = elemental_stress.select(element_ids=[5, 6, 7])
# BREAK BLOCK

simulation = post.StaticMechanicalSimulation(example_path)
print(simulation)
displacement = simulation.displacement()
# BREAK BLOCK

simulation = post.ModalMechanicalSimulation(example_path)
# Print natural frequencies
print(simulation.time_freq_support)
# BREAK BLOCK

simulation = post.TransientMechanicalSimulation(example_path)
print(simulation)
# Query the displacement vectorial field for all times
displacement = simulation.displacement(all_sets=True)
# Animation shows the norm of vectorial fields with several components
displacement.animate(deform=True, title="U")
# BREAK BLOCK

simulation = post.HarmonicMechanicalSimulation(example_path)
print(simulation.time_freq_support)
displacement = simulation.displacement(set_ids=[1, 2])
subdisp = displacement.select(complex=0, set_ids=1)
subdisp.plot(title="U tot real")
subdisp = displacement.select(complex=1, set_ids=1)
subdisp.plot(title="U tot imaginary")
# BREAK BLOCK

# Instantiate the solution object
example_path = examples.find_static_rst()
simulation = post.load_simulation(example_path)
displacement_norm = simulation.displacement(norm=True)
# Plot the data and save the image
displacement_norm.plot(screenshot="total_disp.png")
# BREAK BLOCK

simulation = post.StaticMechanicalSimulation(example_path)
# Extract a result as a Dataframe
displacement_dataframe = simulation.displacement(all_sets=True)
# BREAK BLOCK

print(displacement_dataframe.columns)
# BREAK BLOCK

print(displacement_dataframe.columns.results_index)
print(displacement_dataframe.columns[0].values)
# BREAK BLOCK

displacement_dataframe.display_max_rows = 9
print(displacement_dataframe)
# BREAK BLOCK

disp_X_1 = displacement_dataframe.select(
    set_ids=[1], node_ids=[4872, 9005], components=["X"]
)
print(disp_X_1)
# BREAK BLOCK

print(disp_X_1.array)
# Plot a Dataframe
displacement_dataframe.plot()
# Animate a transient Dataframe
displacement_dataframe.animate()
# BREAK BLOCK
