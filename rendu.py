import bpy
from math import tan
import os
from PIL.Image import core

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

for i in range(1, 5):
    img = core.open(paths + f"bat_{i}.png") #Ouverture de l'image initiale.

    size_x = 1920
    size_y = 1080

    img2 = core.new('RGBA', (size_x,size_y),(255,255,255,255)) # Création de l'image de sortie
    for x in range(0,size_x,1):
        for y in range(0,size_y,1):
            RVBA=img.getpixel((x,y))
            if (RVBA[0] + RVBA[1] + RVBA[1]) / 3 < 5:
                col = (0, 0, 0, 255)
            else:
                col = (255, 255, 255, 0)
            img2.putpixel((x,y),col)


    img.close()
    img2.save(paths + f"bat_clean_{i}.png", "png") # On enregistre l'image finale
    img2.close()