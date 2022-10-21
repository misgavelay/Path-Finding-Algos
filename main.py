import pygame, sys
from button import Button
import dijkstra
import grid_functions as grid

pygame.init()

#READ_ME:
#Left mouse click builds wall
#Richt mouse click sets target
#Space on key board starts algo
#P pauses algo
#C on key board clears board
#Esc on key board sends back to menu

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")
main_font = pygame.font.SysFont("cambria", 30)


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (100, 60)) #resizes the image

GRID = []
PATH = []

GRID = grid.build_grid()


def main_menu():
    while True:
        #screen.blit(BG, (0, 0))
        screen.fill((33,47,135))
        
        
        menu_mouse_pos = pygame.mouse.get_pos()   #mouse position
        
        
        menu_text = main_font.render("Main Menu", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(300, 100))
        
        #Define butons for main menu
        dijkstra_button = Button(image=button_surface, x_pos=300, y_pos=200,      ###what does image = do??
                             text_input="Dijkstra",)
        #options_button = Button(image=button_surface, x_pos=300, y_pos=350,
                              #  text_input="Options")
        quit_button = Button(image=button_surface, x_pos=300, y_pos=500,
                             text_input="Quit")

        screen.blit(menu_text, menu_rect)
        
        #Loop to change collors when hovering over buttons
        for button in [dijkstra_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dijkstra_button.checkForInput(menu_mouse_pos):
                     dijkstra.dijkstra_algo(GRID,PATH)
                     main_menu()
                # if options_button.checkForInput(menu_mouse_pos):
                #     options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
