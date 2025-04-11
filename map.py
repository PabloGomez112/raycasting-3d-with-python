import random
import pygame
from settings import *



class Map:
    GRID_PADDING = 1 # Represents the size of the grid divisions
    MAX_ITERATIONS_FOR_GENERATION = 1000
    def __init__(self):
        self.grid = [[1 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.spawn_x = 0
        self.spawn_y = 0
        self.generate_map()

    def generate_map(self):
        init_x, init_y = random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1)
        self.spawn_x, self.spawn_y = init_x, init_y

        for i in range(self.MAX_ITERATIONS_FOR_GENERATION):
                self.grid[init_y][init_x] = 0
                init_x += random.randint(-1, 1)
                init_y += random.randint(-1, 1)
                init_x = max(0, min(COLUMNS - 1,init_x))
                init_y = max(0, min(ROWS - 1, init_y))

        self.grid[self.spawn_y][self.spawn_x] = 2

    def get_spawn_position(self) -> tuple:
        """
        :return: (spawnX, spawnY)
        """
        return self.spawn_x, self.spawn_y

    def has_wall_at(self, x, y):
        if (0 <= y // TILE_SIZE < ROWS) and (0 <= x // TILE_SIZE < COLUMNS):
            return self.grid[int(y // TILE_SIZE)][int(x // TILE_SIZE)] == 1
        else:
            return False

    def render(self, screen):
        for i in range(ROWS):
            for j in range(COLUMNS):
                tile_x = j * TILE_SIZE
                tile_y = i * TILE_SIZE

                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y,
                                                               TILE_SIZE - self.GRID_PADDING,
                                                               TILE_SIZE - self.GRID_PADDING))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (40, 40, 40), (tile_x, tile_y, TILE_SIZE - self.GRID_PADDING,
                                                            TILE_SIZE - self.GRID_PADDING))
                elif self.grid[i][j] == 2:
                    pygame.draw.rect(screen, (128, 50, 50), (tile_x, tile_y, TILE_SIZE - self.GRID_PADDING,
                                                            TILE_SIZE - self.GRID_PADDING))