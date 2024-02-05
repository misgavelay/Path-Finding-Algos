import pygame , sys
import constants
import colors
def instructions():
    window = pygame.display.set_mode((constants.window_width, constants.window_height))

    pygame.display.set_caption("Instructions")
    main_font = pygame.font.SysFont("poppins", 35)
    instructions_font = pygame.font.SysFont("poppins", 28)
    instructions_head = main_font.render("Instructions:", True, colors.BLUE_WHITE)
    instructions_head_rect = instructions_head.get_rect(center=(120, 100))

    def blitlines(surf, text, font, color, x, y):
        space_between_lines = 50
        lines = text.split('\n')
        for i, ll in enumerate(lines):
            txt_surface = font.render(ll, True, color)
            surf.blit(txt_surface, (x, y + (i * space_between_lines)))
    instructions_text = "'Esp' = Back to main menu\nFirst Right Mouse Click = Choose starting position\nSecond Right Mouse Click = Choose target\n" \
                        "Left Mouse Click = Build wall\n'Space' = Start search\n 'P' = Pause/Continue\n'C' = Clear board"

    pygame.display.update()
    while True:
        window.fill((33, 47, 135))
        window.blit(instructions_head, instructions_head_rect)
        blitlines(window,instructions_text, instructions_font, colors.BLUE_WHITE, 80,160)
        pygame.display.update()
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:  # if the type of the event that  is happening is quit - quit the window
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
