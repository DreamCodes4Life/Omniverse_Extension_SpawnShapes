import omni.ext
import omni.ui as ui
import omni.kit.commands

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print(f"[techlover.spawn.shapes] some_public_function was called with {x}")
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[techlover.spawn.shapes] MyExtension startup")

        self._window = ui.Window("Shape spawner", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click(form):
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	                    prim_type=form,
	                    above_ground=True)
                    print("clicked")

                ui.Button("Spawn Cube", clicked_fn=lambda: on_click("Cube"))
                ui.Button("Spawn Cone", clicked_fn=lambda: on_click("Cone"))

    def on_shutdown(self):
        print("[techlover.spawn.shapes] MyExtension shutdown")


