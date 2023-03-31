import bpy
from math import tan
import os

bpy.context.view_layer.objects.active = bpy.data.objects["Camera"]
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
bpy.context.scene.render.use_freestyle = True
bpy.context.scene.render.line_thickness_mode = 'ABSOLUTE'
bpy.context.scene.render.line_thickness = 1.2

if os.name == "nt":
    paths = "U:/Images/rendus_blender_"
else:
    paths = "~/rendus_blender_"

l = 15
deg = 0.698132
droit = 1.5708

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = droit
bpy.context.object.location[0] = l
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath=paths+'bat_2.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 2*droit
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = l
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath=paths+'bat_3.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 3*droit
bpy.context.object.location[0] = -l
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath=paths+'bat_4.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 0
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = -l
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath=paths+'bat_1.png'
bpy.ops.render.render(write_still=1)