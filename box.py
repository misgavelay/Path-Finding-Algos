import constants
import pygame
box_width = constants.window_width // constants.cols
box_height = constants.window_height // constants.rows

class Box:
    def __init__(self,i,j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None
        self.g_score = float('inf')
        self.h_score = float('inf')
        self.f_score = float('inf')



    def draw(self,win,color):
       pygame.draw.rect(win, color, (self.x *(box_width) , self.y * (box_height), box_width-2, box_height-2))  # draws a rectangle (the display window to draw on, the color, the postions and borders)


    def set_neighbours(self,grid):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < constants.cols - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < constants.rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])
    def reset_box(self):
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.prior = None
        self.g_score = float('inf')
        self.h_score = float('inf')

    def calc_h_score(self,x,y):
        self.h_score = abs(self.x - x) + abs(self.y - y)

    def calc_f_score(self):
        self.f_score = self.h_score + self.g_score