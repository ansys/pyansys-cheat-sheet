from ansys.pyensight.core import launch_ensight

install = "C:\\Program Files\\ANSYS Inc\\v232"
session = launch_ensight(ansys_installation=install)
# BREAK BLOCK
from ansys.pyensight.core import LocalLauncher

install = "C:\\Program Files\\ANSYS Inc\\v232"
session = LocalLauncher(
    ansys_installation=install,
    batch=False, # Launch interactive GUI
).start()
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
# The "new_case" option allows you to create a new case and load multiple datasets in the same EnSight session.
# BREAK BLOCK

image = session.show("image")
# "image" is a renderable object. Any object returned by the "show()" method is a renderable.
image.browser()


# BREAK BLOCK
session.show("deep_pixel")
session.show("webgl")
session.show("animation")

# BREAK BLOCK
session.show("remote").browser()
session.show("remote").url
# The "url" property is the URL for embedding the renderable in your application. It is available in all renderables, like ``browser()``.
# BREAK BLOCK

export = session.ensight.utils.export
export.image("image.png")
export.image("deep_image.tiff", enhanced=True)
export.animation("animation.mp4")
# BREAK BLOCK

parts = session.ensight.utils.parts
parts.select_parts_by_dimension(3) # 3D parts

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
        [ensight_1D_object], # ENS_PART
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
new_ctx.load("state_in_file.ctxz")
session.restore_context(new_ctx)
# BREAK BLOCK
attr = "COLORBYPALETTE"
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight.objs.core) as core:
    core.PARTS.set_attr(attr, "velocity")
    core.PARTS[0].setattr(attr, "energy")
    core.PARTS["fluid_domain"].set_attr(attr, "tke")
# The "set_attr()" method is available for a list of EnSight objects, while the "setattr()" method is available for a single object.
# BREAK BLOCK
sn = session.ensight.utils.support.scoped_name
with sn(session.ensight.objs.core) as core, sn(
    session.ensight.objs.enums
) as enums:
    # 3D parts border, 2D full
    core.PARTS.set_attr("ELTREPRESENTATION", enums.BORD_FULL)
    # High-quality smooth shading
    core.PARTS.set_attr("SHADING", enums.SHAD_SMOOTH_REFINED)
# BREAK BLOCK
session.ensight.objs.core.HIDDENLINE = True
session.ensight.objs.core.HIDDENLINE_USE_RGB = True
session.ensight.objs.core.HIDDENLINE_RGB = [0.0, 0.0, 0.0]
# BREAK BLOCK
