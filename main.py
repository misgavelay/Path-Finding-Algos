import pygame, sys
from button import Button
from bfs import bfs_algo
from A_star import A_star_algo
import grid_functions as grd
from instructions import instructions
import colors
pygame.init()


# TODO :
# fix code repetition


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")
main_font = pygame.font.SysFont("poppins", 35)


button_surface = pygame.image.load("button.png")
# resizes the image
button_surface = pygame.transform.scale(button_surface, (100, 60))

PATH = []
GRID = grd.build_grid()


def main_menu():
    while True:
        screen.fill((33, 47, 135))

        menu_mouse_pos = pygame.mouse.get_pos()   # mouse position
        menu_text = main_font.render("Main Menu", True,colors.BLUE_WHITE)
        menu_rect = menu_text.get_rect(center=(300, 120))
        
        # Define buttons for main menu
        bfs_button = Button(image=button_surface, x_pos=200, y_pos=220, text_input="bfs")
        A_star_button = Button(image=button_surface, x_pos=400, y_pos=220, text_input="A*", )
        quit_button = Button(image=button_surface, x_pos=200, y_pos=350, text_input="Quit")
        instructions_button = Button(image=button_surface, x_pos=400,y_pos=350,text_input="Instructions")
        screen.blit(menu_text, menu_rect)
        
        # Loop to change colors when hovering over buttons
        for button in [bfs_button, A_star_button, instructions_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bfs_button.checkForInput(menu_mouse_pos):
                     bfs_algo(GRID, PATH)
                     main_menu()
                if A_star_button.checkForInput(menu_mouse_pos):
                     A_star_algo(GRID, PATH)
                if instructions_button.checkForInput(menu_mouse_pos):
                    instructions()
                    main_menu()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()