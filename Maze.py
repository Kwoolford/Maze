import random, pygame, numpy as np

# Maze Dimensions
maze_width, maze_height = 20,20

# Screen Dimensions
width, height = 1000, 1000

# Calculating Cell Size
cell_width = width // maze_width
cell_height = height // maze_height

# Importing Images
# Importing the hero image
hero_image = pygame.image.load('hero.jpg')
hero_image = pygame.transform.scale(hero_image, (cell_width, cell_height))
# Importing the door image
door_image = pygame.image.load('door.jpg')
door_image = pygame.transform.scale(door_image, (cell_width, cell_height))
# Importing the spike image
spike_image = pygame.image.load('spike.jpg')
spike_image = pygame.transform.scale(spike_image, (cell_width, cell_height))
# Importing the wall image
wall_image = pygame.image.load('wall.jpg')
wall_image = pygame.transform.scale(wall_image, (cell_width, cell_height))
# Importing the floor image
floor_image = pygame.image.load('floor.jpg')
floor_image = pygame.transform.scale(floor_image, (cell_width, cell_height))

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

# Creating the mazes and and randomly generating spikes in mazes
def createMazes(difficulty):
    maze1 = MAZE()
    spike1 = Spike(maze1.maze)
    spike1.add_spikes(difficulty)
    print(maze1.maze)

    maze2 = MAZE()
    spike2 = Spike(maze2.maze)
    spike2.add_spikes(difficulty)
    print(maze2.maze)

    maze3 = MAZE()
    spike3 = Spike(maze3.maze)
    spike3.add_spikes(difficulty)
    print(maze3.maze)

    maze4 = MAZE()
    spike4 = Spike(maze4.maze)
    spike4.add_spikes(difficulty)
    print(maze4.maze)

    maze5 = MAZE()
    spike5 = Spike(maze5.maze)
    spike5.add_spikes(difficulty)
    print(maze5.maze)

    maze6 = MAZE()
    spike6 = Spike(maze6.maze)
    spike6.add_spikes(difficulty)
    print(maze6.maze)

    maze7 = MAZE()
    spike7 = Spike(maze7.maze)
    spike7.add_spikes(difficulty)
    print(maze7.maze)

    maze8 = MAZE()
    spike8 = Spike(maze8.maze)
    spike8.add_spikes(difficulty)
    print(maze8.maze)

    maze9 = MAZE()
    spike9 = Spike(maze9.maze)
    spike9.add_spikes(difficulty)
    print(maze9.maze)

    # Adding Doors to mazes in logical 3x3 format
    maze1.maze[9, 19] = 3
    maze1.maze[10, 19] = 3
    maze1.maze[19, 9] = 3
    maze1.maze[19, 10] = 3

    maze2.maze[9, 19] = 3
    maze2.maze[10, 19] = 3
    maze2.maze[19, 9] = 3
    maze2.maze[19, 10] = 3
    maze2.maze[9, 0] = 3
    maze2.maze[10, 0] = 3

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

    # Creating the user in Maze 5
    maze5.maze[10, 10] = 4

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

    # Creating the mazes in a logical 3x3 order
    mazes = np.array([[maze1.maze, maze2.maze, maze3.maze],
                    [maze4.maze, maze5.maze, maze6.maze],
                    [maze7.maze, maze8.maze, maze9.maze]])
    
    # Creating the user in Maze 5
    userChords = (1, 1, 10, 10)
    return mazes, userChords

# Creating the room changing logic
def changeRoom(userChords):
    # For the top left grid
    if userChords[0] == 0 and userChords[1] == 0:
        # For taking a right
        if userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For going down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
    
    # For the top center grid
    elif userChords[0] == 0 and userChords[1] == 1:
        # For taking a right
        if userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 2, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 2, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For taking a left
        elif userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 0, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 0, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

    # For the top right grid
    elif userChords[0] == 0 and userChords[1] == 2:
        # For taking a left
        if userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

    # For the center left grid
    elif userChords[0] == 1 and userChords[1] == 0:
        # For taking a right
        if userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For going down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 0, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 0, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For going up
        elif userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 0, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 0, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
    # For the center grid
    elif userChords[0] == 1 and userChords[1] == 1:
        # For taking a right
        if userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going up
        elif userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 1, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For going left
        elif userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going Down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
    # For the center right grid
    elif userChords[0] == 1 and userChords[1] == 2:
        # For taking a left
        if userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        # For going down
        elif userChords[2] == 18 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 2, 1, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 18 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 2, 1, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going up
        elif userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 2, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (0, 2, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
    # For the bottom left grid
    elif userChords[0] == 2 and userChords[1] == 0:
        # For going up
        if userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 0, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For taking a right
        elif userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
    # For the bottom center grid
    elif userChords[0] == 2 and userChords[1] == 1:
        # For taking a right
        if userChords[2] == 9 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 2, 9, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 18:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 2, 10, 1)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For taking a left
        elif userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 0, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 0, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
        # For going up
        elif userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 1, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        
    # For the bottom right grid
    elif userChords[0] == 2 and userChords[1] == 2:
        # For taking a left
        if userChords[2] == 9 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 9, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 10 and userChords[3] == 1:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (2, 1, 10, 18)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

        # For going up
        elif userChords[2] == 1 and userChords[3] == 9:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 18, 9)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4
        elif userChords[2] == 1 and userChords[3] == 10:
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
            userChords = (1, 2, 18, 10)
            mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 4

    print("I am being initiated")
    return userChords

# Creating the game steps
def upStep(userChords):
    # Begin error checking
    if mazes[userChords[0], userChords[1]][userChords[2] - 1, userChords[3]] == 1:
        print("Cannot move through walls")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2] - 1, userChords[3]] == 2:
        print("You hit a spike!\nInitiate game ending procedure")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2] - 1, userChords[3]] == 0:
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
        mazes[userChords[0], userChords[1]][userChords[2] - 1, userChords[3]] = 4
        userChords = (userChords[0], userChords[1], userChords[2] - 1, userChords[3])
        action = userChords
    return action

def downStep(userChords):
    # Begin error checking
    if mazes[userChords[0], userChords[1]][userChords[2] + 1, userChords[3]] == 1:
        print("Cannot move through walls")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2] + 1, userChords[3]] == 2:
        print("You hit a spike!\nInitiate game ending procedure")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2] + 1, userChords[3]] == 0:
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
        mazes[userChords[0], userChords[1]][userChords[2] + 1, userChords[3]] = 4
        userChords = (userChords[0], userChords[1], userChords[2] + 1, userChords[3])
        action = userChords
    return action

def rightStep(userChords):
    # Begin error checking
    if mazes[userChords[0], userChords[1]][userChords[2], userChords[3] + 1] == 1:
        print("Cannot move through walls")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2], userChords[3] + 1] == 2:
        print("You hit a spike!")
        print("Initiate game ending procedure")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2], userChords[3] + 1] == 0:
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3] + 1] = 4
        userChords = (userChords[0], userChords[1], userChords[2], userChords[3] + 1)
        action = userChords
    return action

def leftStep(userChords):
    # Begin error checking
    if mazes[userChords[0], userChords[1]][userChords[2], userChords[3] - 1] == 1:
        print("Cannot move through walls")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2], userChords[3] - 1] == 2:
        print("You hit a spike!")
        print("Initiate game ending procedure")
        action = userChords
    elif mazes[userChords[0], userChords[1]][userChords[2], userChords[3] - 1] == 0:
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3]] = 0
        mazes[userChords[0], userChords[1]][userChords[2], userChords[3] - 1] = 4
        userChords = (userChords[0], userChords[1], userChords[2], userChords[3] - 1)
        action = userChords
    return action


# Defining colors to be used in the rest of the game
black = (0, 0, 0)
blue = (0, 0, 255)
doorColor = (255, 0, 0)
spikeColor = (50, 50, 50)

# Defining Screen Paremeters
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


# Creating game loop function to get the difficulty from the user
def createTextBox():
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(50, 900, 900, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    # Game loop for text input
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.lower() == 'easy':
                            difficulty = 'easy'
                            done = True
                        elif text.lower() == 'medium':
                            difficulty = 'medium'
                            done = True
                        elif text.lower() == 'hard':
                            difficulty = 'hard'
                            done = True
                        else:
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Display the difficulties above the text box
        difficulty_text = font.render("Enter a difficulty : easy, medium, hard", True, (255, 255, 255))
        screen.blit(difficulty_text, (input_box.x, input_box.y - 50))

        pygame.display.flip()
        clock.tick(30)

    return difficulty

# Assigning Spike quantities to difficulties
difficulty = createTextBox()
if difficulty == 'easy':
    difficulty = 0
elif difficulty == 'medium':
    difficulty = 8
elif difficulty == 'hard':
    difficulty = 16


# Create Mazes and Doors
mazes, userChords = createMazes(difficulty)

# Creating the game step loop
running = True
doorChange = False
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Get gamestep info
                # Begin error checking
                if mazes[userChords[0], userChords[1]][userChords[2] - 1, userChords[3]] == 3:
                    userChords = changeRoom(userChords)
                else:
                    userChords = upStep(userChords)


            elif event.key == pygame.K_DOWN:
                # Begin error checking
                if mazes[userChords[0], userChords[1]][userChords[2] + 1, userChords[3]] == 3:
                    userChords = changeRoom(userChords)
                else:
                    userChords = downStep(userChords)

            elif event.key == pygame.K_LEFT:
                # Begin error checking
                if mazes[userChords[0], userChords[1]][userChords[2], userChords[3] - 1] == 3:
                    userChords = changeRoom(userChords)
                else:
                    userChords = leftStep(userChords)

            elif event.key == pygame.K_RIGHT:
                # Begin error checking
                if mazes[userChords[0], userChords[1]][userChords[2], userChords[3] + 1] == 3:
                    userChords = changeRoom(userChords)
                else:
                    userChords = rightStep(userChords)
    print(userChords[0], userChords[1], userChords[2], userChords[3])

    # Draw the maze the player is in
    for i in range(20):
        for j in range(20):
            if mazes[userChords[0], userChords[1]][i, j] == 1:
                screen.blit(wall_image, (j * cell_width, i * cell_height))
            elif mazes[userChords[0], userChords[1]][i, j] == 0:
                screen.blit(floor_image, (j * cell_width, i * cell_height))
            elif mazes[userChords[0], userChords[1]][i, j] == 2:
                screen.blit(spike_image, (j * cell_width, i * cell_height))
            elif mazes[userChords[0], userChords[1]][i, j] == 3:
                screen.blit(door_image, (j * cell_width, i * cell_height))
            elif mazes[userChords[0], userChords[1]][i, j] == 4:
                screen.blit(hero_image, (j * cell_width, i * cell_height))

    pygame.display.update()
    clock.tick(10)
