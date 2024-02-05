from tkinter import messagebox, Tk
import pygame
import sys
import colors
import constants
import grid_functions as grd
import box
from queue import PriorityQueue

def A_star_algo(grid,path):
    # pygame = library , display = a module inside that library, set_mode = a function inside that module
    window = pygame.display.set_mode((constants.window_width, constants.window_height))
    pygame.display.set_caption("A*")
    queue = PriorityQueue()
    # integer to keep track of which box can first
    count = 0
    start_box_set = False
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
        # The events module handles all possible "events" (key press on the key board, mouse presses etc')
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:  # if the type of the event that  is happening is quit - quit the window
                pygame.quit()
                sys.exit()
            # Mouse Controls
            # Keep track of mouse position
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Draw Wall
                if event.buttons[0] and not begin_search:
                    i = x // box.box_width
                    j = y // box.box_height
                    # make sure not start or target
                    if grid[i][j].start or grid[i][j].target :
                        continue
                    grid[i][j].wall = True
                # Set Start
                if event.buttons[2] and not start_box_set:
                    i = x // box.box_width
                    j = y // box.box_height
                    # make sure not box is not a wall
                    if grid[i][j].wall:
                        continue
                    start_box = grd.set_start_box(grid, i, j)
                    start_box_set = True
                # Set Target
                if event.buttons[2] and not target_box_set:
                    i = x // box.box_width
                    j = y // box.box_height
                    # make sure not wall or start
                    if grid[i][j].start or grid[i][j].wall:
                        continue
                    target_box = grid[i][j]
                    target_pos = [i,j]
                    target_box.target = True
                    target_box_set = True
                    start_box.calc_h_score(i,j)
                    queue.put((start_box.f_score,count,start_box))
                    count += 1
            # Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:  # starts the algorithm if space is pressed
                if event.key == pygame.K_SPACE:
                    begin_search = True
            # Clear board
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    begin_search = False
                    count = 0
                    grd.reset_board(grid, path)
                    queue = PriorityQueue()
                    grd.color_boxes(window, grid, path)

                    start_box_set = False
                    target_box_set = False
                    searching = True
                    target_box = None
            # Pause board
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if begin_search:
                        begin_search = False
                    else:
                        begin_search = True
            # Main Menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    grd.reset_board(grid, path)
                    return 0

        if begin_search:
            if queue.qsize() > 0 and searching:
                current_box = queue.get()[2]
                current_box.visited = True
                # Found target
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior

                else:
                    for neighbour in current_box.neighbours:
                        temp_g_score = current_box.g_score+1
                        if temp_g_score < neighbour.g_score:
                            neighbour.g_score = temp_g_score
                            neighbour.calc_h_score(target_pos[0], target_pos[1])
                            neighbour.calc_f_score()
                            if not neighbour.queued and not neighbour.wall:
                                neighbour.queued = True
                                neighbour.prior = current_box
                                queue.put((neighbour.f_score, count, neighbour))
                                count += 1
            # Queue empty and we did not find target then there is no path
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There is no solution!")
                    searching = False
                    begin_search = False

        window.fill((0, 0, 0))
        grd.color_boxes(window, grid, path)



