import pygame

class GridManager:
    def __init__(self, grid_size, screen_size, active_duration):
        self.grid_size = grid_size
        self.screen_size = screen_size
        self.cell_size = screen_size // grid_size
        self.bg_color = (30, 30, 30)
        self.active_color = (100, 100, 255)
        self.inactive_color = (200, 200, 200)
        self.active_duration = active_duration
        self.grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
        self.active_cell = None
        self.last_click_time = 0
        pygame.init()
        self.screen = pygame.display.set_mode((screen_size, screen_size))
        pygame.display.set_caption("Grid Interaction")

    def draw_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                color = self.active_color if self.grid[row][col] else self.inactive_color
                pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.bg_color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 2)

    def handle_click(self, pos):
        col, row = pos[0] // self.cell_size, pos[1] // self.cell_size
        if self.active_cell is not None:
            prev_row, prev_col = self.active_cell
            self.grid[prev_row][prev_col] = False
        self.grid[row][col] = True
        self.active_cell = (row, col)
        self.last_click_time = pygame.time.get_ticks()

    def reset_grid(self):
        self.grid = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.active_cell = None

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.active_cell and current_time - self.last_click_time > self.active_duration:
            row, col = self.active_cell
            self.grid[row][col] = False
            self.active_cell = None
