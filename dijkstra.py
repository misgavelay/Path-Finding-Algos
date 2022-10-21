from tkinter import messagebox, Tk
import pygame
import sys
import colors    ### I want all of the colors??
import constants
import grid_functions as grd
import box



def dijkstra_algo(grid,path):
    window = pygame.display.set_mode((constants.window_width, constants.window_height))  # pygame = library , display = a moudle inside that library, set_mode = a function inside that moudle                                                                 # allows us to display a window
    pygame.display.set_caption("dijkstra")
    queue = []

    start_box = grd.set_start_box(grid)
    queue.append(start_box)


    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
            for event in pygame.event.get():         #The events moudle handles all possible "events" (key press on thekey board, mouse presses etc')
                # Quit Window
                if event.type == pygame.QUIT:        #if the type of the event that  is happening is quit - quit the window
                    pygame.quit()
                    sys.exit()
                # Mouse Controls
                elif event.type == pygame.MOUSEMOTION:      #if the type of the event is a mouse motion - keep track of where the mouse is
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Draw Wall
                    if event.buttons[0] and not begin_search:                   #if left mouse button is pressed - turn the box in to a wall
                        i = x // box.box_width
                        j = y // box.box_height
                        grid[i][j].wall = True
                    # Set Target
                    if event.buttons[2] and not target_box_set:     #if the left mouse button is pressed - turn the box in to a target
                        i = x // box.box_width
                        j = y // box.box_height
                        target_box = grid[i][j]
                        target_box.target = True
                        target_box_set = True

                        # Start Algorithm
                if event.type == pygame.KEYDOWN and target_box_set:  #starts the algorithim if space is pressed
                    if event.key == pygame.K_SPACE:
                        begin_search = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        begin_search = False
                        grd.reset_board(grid,path)
                        queue = []
                        grd.color_boxes(window, grid, path)


                        start_box = grd.set_start_box(grid)
                        queue.append(start_box)
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
                        begin_search = False
                        grd.reset_board(grid, path)
                        queue = []
                        return 0;




            if begin_search:
                if len(queue) > 0 and searching:
                    current_box = queue.pop(0)
                    current_box.visited = True
                    if current_box == target_box:             #if we reached target box -> tracks back the path buy visitind allow the "priors" untill this point
                        searching = False
                        while current_box.prior != start_box:
                            path.append(current_box.prior)
                            current_box = current_box.prior

                    else:                                    # if the box is not the target -> add all the relevent neighbors to queue
                        for neighbour in current_box.neighbours:
                            if not neighbour.queued and not neighbour.wall: #if the box was already qeued by another box, then the other box is the faster way to get to it and it wont change prior
                                neighbour.queued = True
                                neighbour.prior = current_box
                                queue.append(neighbour)

                else:                                       #if the queue is empty and still searching (we have visted all the boxes we need, and we havnt updated the search to false)->
                    if searching:                           # we finish and display errror message
                        Tk().wm_withdraw()   #closes window
                        messagebox.showinfo("No Solution", "There is no solution!")
                        searching = False

            window.fill((0, 0, 0))
            grd.color_boxes(window, grid,path)

