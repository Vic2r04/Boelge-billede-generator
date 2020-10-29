import pygame
import time
import math
from PIL import Image
import glob
import time


image = Image.open(glob.glob("./billede/*")[0])

rgb = image.convert("RGB")

forstørrer = 2

thiccness = 4

canvas_width = image.size[0]*forstørrer
canvas_height = image.size[1]*forstørrer

background_color = pygame.Color(10, 10, 10, 0)

mellemrum = -1
amplitude = 10

pygame.init()

pygame.display.set_caption("Bølge billede generator")


screen = pygame.display.set_mode((canvas_width, canvas_height))
screen.fill(background_color)


surface = pygame.Surface((canvas_width, canvas_height))
surface.fill(background_color)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, "bølge billede.png")



    surface.fill(background_color)
    tid = time.time()
    for i in range(int(canvas_height/(mellemrum+amplitude))):
        frekvens = 20
        hastighed = 0
        for x in range(0, canvas_width):
            y = int((amplitude*i+(i*(mellemrum+1))) + amplitude*math.sin(frekvens*((float(x)/canvas_width)*(2*math.pi) + (hastighed*time.time()))))
            try:
                pixelFarve = rgb.getpixel((x/forstørrer, y/forstørrer))
            except:
                pass
            
            surface.set_at((x, y), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))
            surface.set_at((x, y+1), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))
            surface.set_at((x, y-1), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))
            surface.set_at((x, y+2), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))
            surface.set_at((x, y-2), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))
    print('frame tog:', time.time()-tid)    

    screen.blit(surface, (0, 0))

    pygame.display.flip()
