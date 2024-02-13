import random, pygame, numpy as np, sys


pygame.init()

class Maze:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        #init display
        self.display = pygame.display.set_mode(self.w,self.h)
        pygame.display.set_caption('Maze')
    


cell_size = 60
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill((93,63,211))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((75,75,75))
    # Point specified is the top left of the surface
    screen.blit(test_surface,(200,250))
    pygame.display.update()
    clock.tick(60)