from PIL import Image

for i in range(1, 5):
    img = Image.open(f"./bat{i}.png") #Ouverture de l'image initiale.

    size_x = 1920
    size_y = 1080

    img2 = Image.new('RGBA', (size_x,size_y),(255,255,255,255)) # Création de l'image de sortie
    for x in range(0,size_x,1):
        for y in range(0,size_y,1):
            RVBA=img.getpixel((x,y))
            if (RVBA[0] + RVBA[1] + RVBA[1]) / 3 < 10:
                col = (0, 0, 0, 255)
            else:
                col = (255, 255, 255, 0)
            img2.putpixel((x,y),col)
                

    img.close()
    img2.save(f"bat_clean{i}.png", "png") # On enregistre l'image finale
    img2.show()
    img2.close()


