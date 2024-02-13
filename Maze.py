import random, pygame, numpy as np, sys


pygame.init()
class HERO:
    self.body = np.array([self.x, self.y])
    def __init__(self):
        self.body = []
    
class SPIKE:
    def __init__(self):
        self.x = random.randint(1,cell_number)
        self.y = random.randint(1,cell_number)
        self.pos = np.array([self.x, self.y])
        # Create an x and y position
        # Draw a triangle
    def draw_spike(self):
        spike_rect = pygame.Rect(self.pos[0]*cell_size,self.pos[1]*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen, (1,1,1), spike_rect)

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

spike = SPIKE()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((75,75,75))
    spike.draw_spike()
    # Point specified is the top left of the surface
    pygame.display.update()
    clock.tick(60)