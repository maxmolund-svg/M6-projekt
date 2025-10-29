import pygame
import sys

pygame.init()
surface = pygame.display.set_mode((300, 300)) # window
color = (255, 0, 0)


surface.fill((255, 255, 255))

pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60), 2)

pygame.display.flip()

startTicks = pygame.time.get_ticks()
while pygame.time.get_ticks() - startTicks < 3000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()