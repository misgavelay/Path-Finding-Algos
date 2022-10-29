import constants
from box import Box
import colors
import pygame
def reset_board(grid,path):
    path.clear()
    reset_grid(grid)

def reset_grid(grid):
    for i in range(constants.cols):
        for j in range(constants.rows):
            grid[i][j].reset_box()




#Draws the board again with the correct colors
def color_boxes(window,grid,path):
    for i in range(constants.cols):  # will collor all the boxes the whey we need
        for j in range(constants.rows):
            box = grid[i][j]  # grid
            box.draw(window, colors.GRAY)

            if box.queued:  # next boxes that need to be visited red
                box.draw(window, colors.LIGHT_BLUE)
            if box.visited:  # visited green
                box.draw(window,colors.BLUE)
            if box in path:  # path blue
                box.draw(window, colors.LIGHT_TURKIZ_GREEN)
            if box.start:  # start box trukiz
                box.draw(window, colors.TURKIZ_GREEN)
            if box.wall:  # walls black
                box.draw(window, colors.BLACK)
            if box.target:  # target in yellow
                box.draw(window, colors.WHITE)

    pygame.display.flip()  # updates the surface


#Builds a grid and returns it
def build_grid():
    # Create Grid  -   we create an array of arrays wich the inner arrays are field with boxes. grid = [[box(0,1),box(0,2)...][box(1,0),box(2,0)]////]
    grid = []
    for i in range(constants.cols):
        arr = []
        for j in range(constants.rows):
            arr.append(Box(i, j))
        grid.append(arr)
    # Set Neighbours - for each box in the grid we "notify it" who are his neighbours
    for i in range(constants.cols):
        for j in range(constants.rows):
            grid[i][j].set_neighbours(grid)
    return grid


def set_start_box(grid):
    start_box = grid[0][0]
    start_box.start = True
    start_box.visited = True
    start_box.g_score = 0
    return start_box