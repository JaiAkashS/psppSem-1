import pygame 
pygame.init() 
screen = pygame.display.set_mode((400,400))
screen.fill((0, 0, 0))
pygame.draw.rect(screen, (255,255,255), [75, 10, 50, 20], 2)
pygame.draw.rect(screen, (255,0,0), [75, 150, 150,75]) 
pygame.display.flip() 
