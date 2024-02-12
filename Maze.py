import random, pygame, numpy

pygame.init()

class Direction():
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class MazeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        #init display
        self.display = pygame.display.set_mode(self.w,self.h)
        pygame.display.set_caption('Maze')
    
    def _update_ui(self):
        self.display.fill(BLACK)

    def play_step(self)
if __name__ == '__main__':
    game = MazeGame()

    # Game Loop
    while True:
        game