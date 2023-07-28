from ansys.pyensight.core import launch_ensight
session = launch_ensight(ansys_installation="C:\\Program Files\\ANSYS Inc\\v232")
# BREAK BLOCK
from ansys.pyensight.core import LocalLauncher
launcher = LocalLauncher(ansys_installation="C:\\Program Files\\ANSYS Inc\\v232", batch=False)
session = launcher.start()
# BREAK BLOCK
from ansys.pyensight.core import DockerLauncher
launcher = DockerLauncher(data_directory="d:/data")
launcher.pull()
session = launcher.start()
# BREAK BLOCK

session.load_example("elbow_dp0_dp1.ens")
# BREAK BLOCK

session.load_data("dataset.encas")
session.load_data("dataset.dvs")
session.load_data("dataset.cas.h5", result_file="dataset.dat.h5")
session.load_data("dataset.rst", new_case=True)
# BREAK BLOCK

image = session.show("image")
image.browser()


# BREAK BLOCK
session.show("deep_pixel")
session.show("webgl")
session.show("animation")

# BREAK BLOCK
session.show("remote").browser()
session.show("remote").url

# BREAK BLOCK

export = session.ensight.utils.export
export.image("C:\\Users\\JohnDoe\\Documents\\image.png")
export.image("C:\\Users\\JohnDoe\\Documents\\deep_image.tiff")
export.animation("C:\\Users\\JohnDoe\\Documents\\animation.mp4")
# BREAK BLOCK

parts = session.ensight.utils.parts
parts.select_parts_by_dimension(3)

# BREAK BLOCK
views = session.ensight.utils.views
views.set_view_direction(1,1,1)
# BREAK BLOCK

sn = session.ensight.utils.support.scoped_name
zclip_state = None
with sn(session.ensight) as ensight, sn(session.ensight.objs.core) as core:
    query.create_distance("my_query", query.DISTANCE_PART1D, [ensight_1D_object], core.VARIABLES["my_variable"][0], new_plotter=True)
# BREAK BLOCK
state = session.capture_context()
session.restore_context(state)
state.save("state_on_file.ctxz")
new_ctx = EnsContext()
new_ctx.load("state_on_file.ctxz")
session.restore_context(new_ctx)
# BREAK BLOCK
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight) as ensight, sn(session.ensight.objs.core) as core:
    core.PARTS.set_attr("COLORBYPALETTE", "velocity")
    core.PARTS[0].setattr("COLORBYPALETTE", "pressure")
    core.PARTS["fluid_domain"].set_attr("COLORBYPALETTE", "tke")
    core.PARTS.set_attr("ELTREPRESENTATION", ensight.objs.enums.BORD_FULL)
    core.PARTS.set_attr("SHADING", ensight.objs.enums.SHAD_SMOOTH_REFINED)
    core.HIDDENLINE = True
    core.HIDDENLINE_USE_RGB = True
    core.HIDDENLINE_RGB = [0., 0., 0.]
# BREAK BLOCK