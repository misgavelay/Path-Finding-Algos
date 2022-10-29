import pygame, sys
from button import Button
from dijkstra import dijkstra_algo
from A_star import A_star_algo
import grid_functions as grd

pygame.init()

#READ_ME:
#Left mouse click builds wall
#Richt mouse click sets target
#Space on key board starts algo
#P pauses algo
#C on key board clears board
#Esc on key board sends back to menu

#TODO: anble to choose start position
#instrunctions at the begining
# change constans to caplocks


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")
main_font = pygame.font.SysFont("poppins", 35)


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (100, 60)) #resizes the image

GRID = []
PATH = []

GRID = grd.build_grid()




def main_menu():
    while True:
        screen.fill((33,47,135))
        
        
        menu_mouse_pos = pygame.mouse.get_pos()   #mouse position
        
        
        menu_text = main_font.render("Main Menu", True,(242,251,252))
        menu_rect = menu_text.get_rect(center=(300, 100))
        
        #Define butons for main menu
        dijkstra_button = Button(button_surface, 300, 200,
                             "Dijkstra",)
        #options_button = Button(image=button_surface, x_pos=300, y_pos=350,
                              #  text_input="Options")
        A_star_button = Button(button_surface, 300, 300,
                                 "A*", )
        quit_button = Button(image=button_surface, x_pos=300, y_pos=400,
                             text_input="Quit")

        screen.blit(menu_text, menu_rect)
        
        #Loop to change collors when hovering over buttons
        for button in [dijkstra_button,A_star_button,quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dijkstra_button.checkForInput(menu_mouse_pos):
                     dijkstra_algo(GRID,PATH)
                     main_menu()
                if A_star_button.checkForInput(menu_mouse_pos):
                     A_star_algo(GRID,PATH)
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()