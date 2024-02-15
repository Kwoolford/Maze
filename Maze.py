import random, pygame, numpy as np

# Maze Dimensions
maze_width, maze_height = 20,20

# Screen Dimensions
width, height = 1000, 1000

# Calculating Cell Size
cell_width = width // maze_width
cell_height = height // maze_height

# Initialize Pygame
pygame.init()    

class MAZE:
    def __init__(self):
        self.maze = np.zeros((maze_width, maze_height), dtype=int)

        # Add walls to the maze
        self.maze[0,:] = 1
        self.maze[:,0] = 1
        self.maze[-1,:] = 1
        self.maze[:,-1] = 1
        print(self.maze)


# Creating Spike Class to add spikes to mazes
class Spike:
    def __init__(self, maze):
        self.maze = maze

    def add_spike(self):
        x = random.randint(2, maze_width - 3)
        y = random.randint(2, maze_height - 3)
        while self.maze[x, y] != 0:
            x = random.randint(2, maze_width - 3)
            y = random.randint(2, maze_height - 3)
        self.maze[x, y] = 2
    
    def add_spikes(self, num_spikes):
        for _ in range(num_spikes):
            self.add_spike()

class User:
    def __init__(self, maze):
        # Initialize User object with maze and starting position at the center
        self.maze = maze
        self.x = maze_width // 2
        self.y = maze_height // 2
        self.maze[self.x, self.y] = 4

    def move_up(self):
        # Move user up if the cell above is not a wall
        if self.maze[self.x - 1, self.y] != 1:
            self.maze[self.x, self.y] = 0
            self.x -= 1
            self.maze[self.x, self.y] = 4

    def move_down(self):
        # Move user down if the cell below is not a wall
        if self.maze[self.x + 1, self.y] != 1:
            self.maze[self.x, self.y] = 0
            self.x += 1
            self.maze[self.x, self.y] = 4

    def move_left(self):
        # Move user left if the cell to the left is not a wall
        if self.maze[self.x, self.y - 1] != 1:
            self.maze[self.x, self.y] = 0
            self.y -= 1
            self.maze[self.x, self.y] = 4

    def move_right(self):
        # Move user right if the cell to the right is not a wall
        if self.maze[self.x, self.y + 1] != 1:
            self.maze[self.x, self.y] = 0
            self.y += 1
            self.maze[self.x, self.y] = 4
# Creating the mazes and and randomly generating spikes in mazes

maze1 = MAZE()
spike1 = Spike(maze1.maze)
spike1.add_spikes(5)
print(maze1.maze)

maze2 = MAZE()
spike2 = Spike(maze2.maze)
spike2.add_spikes(5)
print(maze2.maze)

maze3 = MAZE()
spike3 = Spike(maze3.maze)
spike3.add_spikes(5)
print(maze3.maze)

maze4 = MAZE()
spike4 = Spike(maze4.maze)
spike4.add_spikes(5)
print(maze4.maze)

maze5 = MAZE()
spike5 = Spike(maze5.maze)
spike5.add_spikes(5)
print(maze5.maze)

maze6 = MAZE()
spike6 = Spike(maze6.maze)
spike6.add_spikes(5)
print(maze6.maze)

maze7 = MAZE()
spike7 = Spike(maze7.maze)
spike7.add_spikes(5)
print(maze7.maze)

maze8 = MAZE()
spike8 = Spike(maze8.maze)
spike8.add_spikes(5)
print(maze8.maze)

maze9 = MAZE()
spike9 = Spike(maze9.maze)
spike9.add_spikes(5)
print(maze9.maze)


# Modifying mazes to create doors in correct locations
# Adding Doors to mazes in logical 3x3 format
maze1.maze[9, 19] = 3
maze1.maze[10, 19] = 3
maze1.maze[19, 9] = 3
maze1.maze[19, 10] = 3

maze2.maze[9, 19] = 3
maze2.maze[10, 19] = 3
maze2.maze[19, 9] = 3
maze2.maze[19, 10] = 3
maze2.maze[0, 9] = 3
maze2.maze[0, 10] = 3

maze3.maze[19, 9] = 3
maze3.maze[19, 10] = 3
maze3.maze[9, 0] = 3
maze3.maze[10, 0] = 3

maze4.maze[9, 19] = 3
maze4.maze[10, 19] = 3
maze4.maze[19, 9] = 3
maze4.maze[19, 10] = 3
maze4.maze[0, 9] = 3
maze4.maze[0, 10] = 3

maze5.maze[9, 19] = 3
maze5.maze[10, 19] = 3
maze5.maze[19, 9] = 3
maze5.maze[19, 10] = 3
maze5.maze[0, 9] = 3
maze5.maze[0, 10] = 3
maze5.maze[9, 0] = 3
maze5.maze[10, 0] = 3

maze6.maze[0, 9] = 3
maze6.maze[0, 10] = 3
maze6.maze[9, 0] = 3
maze6.maze[10, 0] = 3
maze6.maze[19, 9] = 3
maze6.maze[19, 10] = 3

maze7.maze[9, 19] = 3
maze7.maze[10, 19] = 3
maze7.maze[0, 9] = 3
maze7.maze[0, 10] = 3

maze8.maze[9, 19] = 3
maze8.maze[10, 19] = 3
maze8.maze[0, 9] = 3
maze8.maze[0, 10] = 3
maze8.maze[9, 0] = 3
maze8.maze[10, 0] = 3

maze9.maze[0, 9] = 3
maze9.maze[0, 10] = 3
maze9.maze[9, 0] = 3
maze9.maze[10, 0] = 3
# Creating the user
player = User(maze5.maze)

# Creating the array of mazes
mazes = np.array([[maze1.maze, maze2.maze, maze3.maze],
                  [maze4.maze, maze5.maze, maze6.maze],
                  [maze7.maze, maze8.maze, maze9.maze]])

# Defining colors to be used in the rest of the game
black = (0, 0, 0)
blue = (0, 0, 255)
doorColor = (255, 0, 0)
spikeColor = (50, 50, 50)

# Defining Screen Paremeters
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Creating the game step loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # Draw the maze the player is in
    mazenum = mazes[1, 1]
    print("This is printing maze 1")
    print(mazenum)
    for i in range(20):
        for j in range(20):
            if mazenum[i, j] == 1:
                color = black
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif mazenum[i, j] == 0:
                color = blue
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif mazenum[i, j] == 2:
                color = spikeColor
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif mazenum[i, j] == 3:
                color = doorColor
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
            elif mazenum[i, j] == 4:
                color = (0, 255, 0)
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))

    pygame.display.update()
    clock.tick(100)
