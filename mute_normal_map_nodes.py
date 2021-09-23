import bpy
from bpy.props import EnumProperty

bl_info = {
    "name": "Toggle Normal Map Nodes",
    "description": "Allows for toggling all Normal Maps OFF, to improve EEVEE viewport performance and later back ON for render output.",
    "author": "crute",
    "blender": (2, 80, 0),
    "location": "Tools Panel (T) in Shader/Node Editor",
    "wiki_url": "https://developer.blender.org/T64458",
    "category": "Material",
}


class MUT_OT_normal_map_nodes(bpy.types.Operator):
    bl_description = "Toggle all normal map nodes off/on"
    bl_idname = "nodes.muting"
    bl_label = "Un/Mute Normal Map nodes"
    bl_options = set({"REGISTER", "UNDO"})

    mute:EnumProperty(
        items=[
            ("off", "Off", "Disable all"),
            ("on", "On", "Enable all"),
            ("toggle", "Toggle", "Invert values"),
        ],
        name="Un/Mute",
        description="Mode to set for all normal map nodes",
        default="toggle",
        options=set({"SKIP_SAVE"}),
    )

    @classmethod
    def poll(self, context):
        return bpy.data.materials

    def invoke(self, context, event):
        return self.execute(context)

    def execute(self, context):
        if self.mute == "toggle":
            mute = None
        elif self.mute == "off":
            mute = False
        elif self.mute == "on":
            mute = True
        for mat in bpy.data.materials:
            nodes = getattr(mat.node_tree, "nodes", [])
            for node in nodes:
                if isinstance(node, bpy.types.ShaderNodeNormalMap):
                    if mute is None:
                        mute = node.mute
                    node.mute = not mute
        return {"FINISHED"}


class MUT_PT_normal_map_nodes(bpy.types.Panel):
    bl_category = ""
    bl_label = ""
    bl_options = set({"HIDE_HEADER"})
    bl_region_type = "TOOLS"
    bl_space_type = "NODE_EDITOR"

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        layout.operator("nodes.muting", text="On").mute = "on"
        layout.operator("nodes.muting", text="Off").mute = "off"
        layout.operator("nodes.muting", text="Toggle").mute = "toggle"


classes = (
    MUT_OT_normal_map_nodes,
    MUT_PT_normal_map_nodes,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
