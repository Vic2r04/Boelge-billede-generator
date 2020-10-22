import pygame
import time
import math
from PIL import Image
import glob


image = Image.open(glob.glob("./billede/*")[0])

rgb = image.convert("RGB")


canvas_width = image.size[0]
canvas_height = image.size[1]

background_color = pygame.Color(0, 0, 0, 0)

mellemrum = -1
amplitude = 5 

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

    surface.fill(background_color)

    for i in range(int(canvas_height/(mellemrum+amplitude))):
        frekvens = 20
        hastighed = 0
        for x in range(0, canvas_width):
            y = int((amplitude*i+(i*(mellemrum+1))) + amplitude*math.sin(frekvens*((float(x)/canvas_width)*(2*math.pi) + (hastighed*time.time()))))
            try:
                pixelFarve = rgb.getpixel((x, y))
            except:
                pass
            surface.set_at((x, y), pygame.Color(pixelFarve[0], pixelFarve[1], pixelFarve[2], 0))

    # Put the surface we draw on, onto the screen
    screen.blit(surface, (0, 0))

    # Show it.
    pygame.display.flip()
