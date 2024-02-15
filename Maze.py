import random, pygame, numpy as np

# Maze Dimensions
maze_width, maze_height = 20,20

# Screen Dimensions
width, height = 1000, 1000

# Calculating Cell Size
cell_width = width // maze_width
cell_height = height // maze_height

pygame.init()    
class SPIKE:
    def __init__(self):
        self.x = random.randint(2, maze_width - 3)
        self.y = random.randint(2, maze_height - 3)
        self.pos = self.x, self.y
        # Create an x and y position
        # Draw a triangle
    def draw_spike(self):
        spike_rect = pygame.Rect(self.pos[0]*cell_width,self.pos[1]*cell_height,cell_width,cell_height)
        pygame.draw.rect(screen, (1,1,1), spike_rect)


class MAZE:
    def __init__(self):
        self.maze = np.zeros((maze_width, maze_height), dtype=int)

        # Add walls to the maze
        self.maze[0,:] = 1
        self.maze[:,0] = 1
        self.maze[-1,:] = 1
        self.maze[:,-1] = 1
        print(self.maze)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

spike = SPIKE()
# Creating the mazes and array of mazes
maze1 = MAZE()
maze2 = MAZE()
maze3 = MAZE()
maze4 = MAZE()
maze5 = MAZE()
maze6 = MAZE()
maze7 = MAZE()
maze8 = MAZE()
maze9 = MAZE()
mazes = np.array([[maze1.maze, maze2.maze, maze3.maze],
                  [maze4.maze, maze5.maze, maze6.maze],
                  [maze7.maze, maze8.maze, maze9.maze]])


# Defining colors to be used in the rest of the game
black = (0, 0, 0)
blue = (0, 0, 255)
doorColor = (255, 0, 0)


# Creating the game step loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    spike.draw_spike()

    # Draw the maze the player is in
    for i in range(20):
        for j in range(20):
            if maze1.maze[i, j] == 1:
                color = black
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif maze1.maze[i, j] == 0:
                color = blue
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif maze1.maze[i, j] == 2:
                color = doorColor
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))

    pygame.display.update()
    clock.tick(60)
