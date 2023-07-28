from ansys.pyensight.core import launch_ensight

install = "C:\\Program Files\\ANSYS Inc\\v232"
session = launch_ensight(ansys_installation=install)
# BREAK BLOCK
from ansys.pyensight.core import LocalLauncher

install = "C:\\Program Files\\ANSYS Inc\\v232"
session = LocalLauncher(
    ansys_installation=install,
    batch=False,
).start()
# Setting batch=False will also launch the full EnSight GUI.
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
session.load_data("out.cas.h5", result_file="data.dat.h5")
session.load_data("dataset.rst", new_case=True)
# The "new_case" option allows to create a new case and load multiple datasets in the same EnSight session.
# BREAK BLOCK

image = session.show("image")
# image is a Renderable object. Any object returned by show is a Renderable.
image.browser()


# BREAK BLOCK
session.show("deep_pixel")
session.show("webgl")
session.show("animation")
# Use browser() to display the renderable in a browser

# BREAK BLOCK
session.show("remote").browser()
session.show("remote").url
# The "url" property is the URL to embed the Renderable in your application. It is available to all the Renderables
# BREAK BLOCK

export = session.ensight.utils.export
export.image("image.png")
export.image("deep_image.tiff")
export.animation("animation.mp4")
# BREAK BLOCK

parts = session.ensight.utils.parts
parts.select_parts_by_dimension(3)

# BREAK BLOCK
views = session.ensight.utils.views
views.set_view_direction(1, 1, 1)
# BREAK BLOCK

query = session.ensight.utils.query
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight.objs.core) as core:
    query.create_distance(
        "my_query",
        query.DISTANCE_PART1D,
        [ensight_1D_object],
        core.VARIABLES["my_variable"][0],
        new_plotter=True,
    )
# BREAK BLOCK
state = session.capture_context()
# BREAK BLOCK
state.save("state_on_file.ctxz")
# BREAK BLOCK
session.restore_context(state)
# BREAK BLOCK
new_ctx = EnsContext()
new_ctx.load("state_on_file.ctxz")
session.restore_context(new_ctx)
# BREAK BLOCK
attr = "COLORBYPALETTE"
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight.objs.core) as core:
    core.PARTS.set_attr(attr, "velocity")
    core.PARTS[0].setattr(attr, "energy")
    core.PARTS["fluid_domain"].set_attr(attr, "tke")
# set_attr() is a method available for a list of EnSight Objects, while setattr() is a method available for the single object
# BREAK BLOCK
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight.objs.core) as core, sn(
    session.ensight.objs.enums
) as enums:
    core.PARTS.set_attr("ELTREPRESENTATION", enums.BORD_FULL)
    core.PARTS.set_attr("SHADING", enums.SHAD_SMOOTH_REFINED)
# BREAK BLOCK
session.ensight.objs.core.HIDDENLINE = True
session.ensight.objs.core.HIDDENLINE_USE_RGB = True
session.ensight.objs.core.HIDDENLINE_RGB = [0.0, 0.0, 0.0]
# BREAK BLOCK
