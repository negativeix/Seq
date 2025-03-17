import pygame
import sys
from mode import Mode
from grid_manager import GridManager


class Game:
    def __init__(self):
        self.mode = Mode()
        self.grid_manager = GridManager(grid_size=3, screen_size=600,
                                        active_duration=500)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.grid_manager.handle_click(pygame.mouse.get_pos())

    def update_game(self):
        self.grid_manager.update()

    def draw_game(self):
        self.grid_manager.draw_grid()
        pygame.display.flip()

    def next_level(self):
        self.mode.next_level()
        self.grid_manager.reset_grid()

    def run(self):
        while self.running:
            self.handle_events()
            self.update_game()
            self.draw_game()

            # Example: Move to next level every 5 seconds
            if pygame.time.get_ticks() > 5000:
                self.next_level()

            pygame.time.Clock().tick(60)  # Set FPS

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
