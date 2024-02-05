from tkinter import messagebox, Tk
import pygame
import sys
import constants
import grid_functions as grd
import box



def bfs_algo(grid,path):
    # pygame = library , display = a module inside that library, set_mode = a function inside that modUle
    window = pygame.display.set_mode((constants.window_width, constants.window_height))
    pygame.display.set_caption("bfs")

    queue = []
    begin_search = False
    start_box_set = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
        # The events module handles all possible "events" (key press on the key board, mouse presses etc')
            for event in pygame.event.get():
                # Quit Window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Mouse Controls
                elif event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Draw Wall
                    if event.buttons[0] and not begin_search:
                        i = x // box.box_width
                        j = y // box.box_height
                        # make sure not start or target
                        if grid[i][j].start or grid[i][j].target:
                            continue
                        grid[i][j].wall = True
                    # Set Start
                    if event.buttons[2] and not start_box_set:
                        i = x // box.box_width
                        j = y // box.box_height
                        # make sure not wall
                        if grid[i][j].wall:
                            continue
                        start_box = grd.set_start_box(grid,i,j)
                        queue.append(start_box)
                        start_box_set = True
                    # Set Target
                    if event.buttons[2] and not target_box_set and start_box_set:
                        i = x // box.box_width
                        j = y // box.box_height
                        # make sure it is not the start box or wall
                        if grid[i][j].start or grid[i][j].wall:
                            continue
                        target_box = grid[i][j]
                        target_box.target = True
                        target_box_set = True

                # Start Algorithm
                if event.type == pygame.KEYDOWN and target_box_set:
                    if event.key == pygame.K_SPACE:
                        begin_search = True
                # Clear Board
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        begin_search = False
                        grd.reset_board(grid,path)
                        start_box_set = False
                        queue = []
                        grd.color_boxes(window, grid, path)
                        target_box_set = False
                        searching = True
                        target_box = None
                # Pause search
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if begin_search:
                            begin_search = False
                        else:
                            begin_search = True
                # Back to main menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        grd.reset_board(grid, path)
                        return 0

            if begin_search:
                if len(queue) > 0 and searching:
                    current_box = queue.pop(0)
                    current_box.visited = True
                    # Found target
                    if current_box == target_box:
                        searching = False
                        # Trace back the path
                        while current_box.prior != start_box:
                            path.append(current_box.prior)
                            current_box = current_box.prior

                    else:
                        for neighbour in current_box.neighbours:
                            if not neighbour.queued and not neighbour.wall:
                                neighbour.queued = True
                                neighbour.prior = current_box
                                queue.append(neighbour)
                # Queue empty and we did not find target then there is no path
                else:
                    if searching:
                        Tk().wm_withdraw()
                        messagebox.showinfo("No Solution", "There is no solution!")
                        searching = False
                        begin_search = False

            window.fill((0, 0, 0))
            grd.color_boxes(window, grid,path)

