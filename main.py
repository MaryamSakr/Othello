import pygame
from GameState import GameState
from HomeScreen import HomeScreen
from instructionsScreen import InstructionScreen

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

def main():
    clock = pygame.time.Clock()
    home_state = HomeScreen()
    instruction_state = InstructionScreen()
    game_state = None
    current_state = "home"

    while True:
        events = pygame.event.get()

        if current_state == "home":
            next_state = home_state.handle_events(events)
            if next_state:
                current_state = next_state

        elif current_state == "instruction":
            next_state = instruction_state.handle_events(events)
            if next_state:
                game_state = GameState(home_state.name_input_text, home_state.choose_input_text , home_state.level_input_text)
                current_state = next_state
        elif current_state == "game":
            next_state = game_state.handle_events(events)
            if next_state:
                current_state = next_state

        screen.fill(black)

        if current_state == "home":
            home_state.draw()

        elif current_state == "instruction":
            instruction_state.draw()

        elif current_state == "game":
            game_state.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
