import sys

import pygame

pygame.init()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Othello")

# Define fonts
font_large = pygame.font.SysFont(None, 36)
font_small = pygame.font.SysFont(None, 24)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 107, 50)
baby_green = (17, 147, 57)

def draw_text(text, font, color, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * font.get_height()))
        screen.blit(text_surface, text_rect)



class InstructionScreen:
    def __init__(self):
        self.name_button_rect = pygame.Rect(screen_width // 2 - 60, screen_height//2, 100, 40)

    def handle_events(self , events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.name_button_rect.collidepoint(event.pos):
                    return "game"

    def draw(self):
        pygame.draw.rect(screen,blue, self.name_button_rect)
        draw_text("Start", font_small, white, screen_width // 2 -10,  screen_height//2 + 20)

        draw_text("Please, follow the instructions .. \nEach player has 30 pieces only. "
              "If they run out, the game ends. \nChoose a cell from the board and enter its "
              "indices as shown in the following board ..", font_small, white, screen_width // 2, screen_height//2 - 100)
