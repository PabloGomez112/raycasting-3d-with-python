import math
import pygame.draw
from vector_utils import Vector2
from utils import deg_to_rad
from settings import TILE_SIZE

class Player:
    def __init__(self, spawn_position):

        self.actual_position = Vector2(spawn_position[0] * TILE_SIZE + (TILE_SIZE / 2),
                                       spawn_position[1] * TILE_SIZE + (TILE_SIZE / 2))

        self.radius_size = 10
        self.view_angle = 0
        self.rotation_speed = deg_to_rad(7)
        self.move_speed = 2
        self.movement_vector = Vector2(0, 0)
        self.turn_direction = 0
        self.walk_direction = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.turn_direction = 0
        self.walk_direction = 0

        if keys[pygame.K_a]:
            self.turn_direction = -1
        if keys[pygame.K_d]:
            self.turn_direction = 1
        if keys[pygame.K_w]:
            self.walk_direction = 1
        if keys[pygame.K_s]:
            self.walk_direction = -1

        move_step = self.walk_direction * self.move_speed
        self.view_angle += self.turn_direction * self.rotation_speed
        self.movement_vector.update_vector(math.cos(self.view_angle) * move_step,
                                           math.sin(self.view_angle) * move_step)

        self.actual_position += self.movement_vector

    def get_position(self) -> Vector2:
        return self.actual_position

    def render(self, screen):
        x = self.actual_position.get_x()
        y = self.actual_position.get_y()

        #pygame.draw.circle(screen, (128, 255, 0), (x, y), self.radius_size)
        """pygame.draw.line(screen, (0, 0, 255), (x, y),
                            (x + math.cos(self.view_angle) * 60,
                                    y + math.sin(self.view_angle)* 60), width=2)"""