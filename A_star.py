from tkinter import messagebox, Tk
import pygame
import sys
import colors
import constants
import grid_functions as grd
import box
from queue import PriorityQueue

def A_star_algo(grid,path):
    window = pygame.display.set_mode((constants.window_width, constants.window_height))  # pygame = library , display = a moudle inside that library, set_mode = a function inside that moudle                                                                 # allows us to display a window
    pygame.display.set_caption("A*")
    queue = PriorityQueue()
    count = 0 #will be used in PriorityQueue.get() to determine between to boxes that have the same f score
    start_box = grd.set_start_box(grid)
 


    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
        for event in pygame.event.get():  # The events moudle handles all possible "events" (key press on thekey board, mouse presses etc')
            # Quit Window
            if event.type == pygame.QUIT:  # if the type of the event that  is happening is quit - quit the window
                pygame.quit()
                sys.exit()
            # Mouse Controls
            elif event.type == pygame.MOUSEMOTION:  # if the type of the event is a mouse motion - keep track of where the mouse is
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Draw Wall
                if event.buttons[0] and not begin_search :  # if left mouse button is pressed - turn the box in to a wall
                    i = x // box.box_width
                    j = y // box.box_height
                    grid[i][j].wall = True
                # Set Target
                if event.buttons[2] and not target_box_set :  # if the left mouse button is pressed - turn the box in to a target
                    i = x // box.box_width
                    j = y // box.box_height
                    target_box = grid[i][j]
                    target_pos = [i,j]
                    target_box.target = True
                    target_box_set = True
                    start_box.calc_h_score(i,j)
                    queue.put((start_box.f_score,count,start_box))
                    count += 1
                    # Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:  # starts the algorithim if space is pressed
                if event.key == pygame.K_SPACE:
                    begin_search = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    begin_search = False
                    count = 0
                    grd.reset_board(grid, path)
                    queue = PriorityQueue()
                    grd.color_boxes(window, grid, path)

                    start_box = grd.set_start_box(grid)

                    target_box_set = False
                    searching = True
                    target_box = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if begin_search:
                        begin_search = False
                    else:
                        begin_search = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    grd.reset_board(grid, path)
                    return 0;

        if begin_search:
            if queue.qsize() > 0 and searching:
                current_box = queue.get()[2]
                current_box.visited = True
                if current_box == target_box:  # if we reached target box -> tracks back the path buy visitind allow the "priors" untill this point
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior

                else:  # if the box is not the target -> add all the relevent neighbors to queue
                    for neighbour in current_box.neighbours:
                        temp_g_score = current_box.g_score+1
                        if(temp_g_score< neighbour.g_score):
                            neighbour.g_score = temp_g_score
                            neighbour.calc_h_score(target_pos[0],target_pos[1])
                            neighbour.calc_f_score()
                            if not neighbour.queued and not neighbour.wall:  # if the box was already qeued by another box, then the other box is the faster way to get to it and it wont change prior
                                neighbour.queued = True
                                neighbour.prior = current_box
                                queue.put((neighbour.f_score,count,neighbour))
                                count += 1

            else:  # if the queue is empty and still searching (we have visted all the boxes we need, and we havnt updated the search to false)->
                if searching:  # we finish and display errror message
                    Tk().wm_withdraw()  # closes window
                    messagebox.showinfo("No Solution", "There is no solution!")
                    searching = False

        window.fill((0, 0, 0))
        grd.color_boxes(window, grid, path)



