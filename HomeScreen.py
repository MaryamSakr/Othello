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


class HomeScreen:
    def __init__(self):
        self.choose_input_text = ""
        self.name_input_text = ""
        self.level_input_text = ""
        self.choose_input_active = False
        self.name_input_active = False
        self.level_input_active = False
        self.choose_field = pygame.Rect(screen_width // 2 - 150, 150, 300, 40)
        self.name_field = pygame.Rect(screen_width // 2 - 150, 250, 300, 40)
        self.level_field = pygame.Rect(screen_width // 2 - 150, 350, 300, 40)
        self.submit_button_rect = pygame.Rect(screen_width // 2 + 175, 450, 100, 40)
        self.choose_button_color = blue
        self.message = "_"

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.choose_field.collidepoint(event.pos):
                    self.choose_input_active = True
                    self.name_input_active = False
                    self.level_input_active = False
                elif self.name_field.collidepoint(event.pos):
                    self.name_input_active = True
                    self.choose_input_active = False
                    self.level_input_active = False
                elif self.level_field.collidepoint(event.pos):
                    self.level_input_active = True
                    self.choose_input_active = False
                    self.name_input_active = False
                elif self.submit_button_rect.collidepoint(event.pos):
                    if self.name_input_text.strip() and self.choose_input_text in ["1", "2"] and self.level_input_text in ["1", "2", "3"]:
                        self.message = "Please, follow the instructions .. \nEach player has 30 pieces only. " \
                                       "If they run out, the game ends. \nChoose cell from the board and enter its " \
                                       "indices as shown in the following board .."
                        return "instruction"
                    else:
                        if not self.name_input_text.strip():
                            self.message = "Please enter your name"
                        if self.choose_input_text not in ["1", "2"]:
                            self.message = "Please enter 1 or 2(Player Number)"
                        if self.level_input_text not in ["1", "2", "3"]:
                            self.message = "Please enter 1 or 2 or 3 (Level)"

            elif event.type == pygame.KEYDOWN:
                if self.choose_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.choose_input_text = self.choose_input_text[:-1]
                    elif event.unicode.isdigit():
                        self.choose_input_text += event.unicode

                elif self.name_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.name_input_text = self.name_input_text[:-1]
                    else:
                        self.name_input_text += event.unicode
                elif self.level_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.level_input_text = self.level_input_text[:-1]
                    else:
                        self.level_input_text += event.unicode

    def draw(self):
        screen.fill(black)

        draw_text("Welcome to Othello!", font_large, white, screen_width // 2, 50)
        draw_text("Player 1 starts (Black) ..", font_small, white, screen_width // 2, 100)
        draw_text("Do you want to be player 1 or 2 ?", font_small, white, screen_width // 2, 130)

        if self.message == "Please enter your name":
            pygame.draw.rect(screen, red, self.name_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.name_field, border_radius=20)
        if self.message == "Please enter 1 or 2(Player Number)":
            pygame.draw.rect(screen, red, self.choose_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.choose_field, border_radius=20)
        if self.message == "Please enter 1 or 2 or 3 (Level)":
            pygame.draw.rect(screen, red, self.level_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.level_field, border_radius=20)

        pygame.draw.rect(screen, white, self.choose_field, border_radius=20)

        draw_text(self.choose_input_text, font_small, black, self.choose_field.centerx, self.choose_field.centery)

        draw_text("Enter Your Name", font_small, white, screen_width // 2, 230)
        pygame.draw.rect(screen, white, self.name_field, border_radius=20)
        draw_text(self.name_input_text, font_small, black, self.name_field.centerx, self.name_field.centery)

        draw_text("(1) Easy. (2) Medium. (3) Hard.", font_small, white, screen_width // 2, 330)
        pygame.draw.rect(screen, white, self.level_field, border_radius=20)
        draw_text(self.level_input_text, font_small, black, self.level_field.centerx, self.level_field.centery)
        pygame.draw.rect(screen, self.choose_button_color, self.submit_button_rect)
        draw_text("Submit", font_small, white, screen_width // 2 + 227, 470)

        draw_text(self.message, font_small, white, screen_width // 2, 450)
