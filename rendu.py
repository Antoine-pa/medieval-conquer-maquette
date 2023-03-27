import bpy
from math import tan

bpy.context.view_layer.objects.active = bpy.data.objects["Camera"]
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
bpy.context.scene.render.use_freestyle = True
bpy.context.scene.render.line_thickness_mode = 'ABSOLUTE'
bpy.context.scene.render.line_thickness = 1.2

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
bpy.context.scene.render.filepath='bat2.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 2*droit
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = l
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath='bat3.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 3*droit
bpy.context.object.location[0] = -l
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath='bat4.png'
bpy.ops.render.render(write_still=1)

bpy.context.object.rotation_euler[0] = droit
bpy.context.object.rotation_euler[1] = 0
bpy.context.object.rotation_euler[2] = 0
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = -l
bpy.context.object.location[2] = l/tan(deg)
bpy.context.object.rotation_euler[0] = deg
scene = bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath='bat1.png'
bpy.ops.render.render(write_still=1)