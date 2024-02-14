import random, pygame, numpy as np

# Maze Dimensions
maze_width, maze_height = 20,20

# Screen Dimensions
width, height = 1000, 1000

# Calculating Cell Size
cell_width = width // maze_width
cell_height = height // maze_height

pygame.init()
class HERO:
    def __init__(self):
        self.body = (10,10)

    def draw_hero(self):
        hero_rect = pygame.Rect(self.body[0]*cell_width, self.body[1]*cell_height, cell_width, cell_height)
        pygame.draw.rect(screen, (255, 0, 0), hero_rect)
    
class MAZE:
    def __init__(self):
        self.maze = np.zeros((maze_width, maze_height))
        self.maze[0] = 1
        self.maze[-1] = 1
        self.maze[:,0] = 1
        self.maze[:,-1] = 1
        print(self.maze)
        # Adding a comment for a test

class SPIKE:
    def __init__(self):
        self.x = random.randint(1,maze_width)
        self.y = random.randint(1,maze_height)
        self.pos = self.x, self.y
        # Create an x and y position
        # Draw a triangle


    def draw_spike(self):
        spike_rect = pygame.Rect(self.pos[0]*cell_width,self.pos[1]*cell_height,cell_width,cell_height)
        pygame.draw.rect(screen, (1,1,1), spike_rect)



screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

spike = SPIKE()
hero = HERO()
maze = MAZE()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
  
    screen.fill((75,75,75))
    spike.draw_spike()
    hero.draw_hero()
    # Point specified is the top left of the surface
    pygame.display.update()
    clock.tick(60)