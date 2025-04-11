import math

import pygame
from settings import *
from ray import Ray

class Raycaster:
    TOTAL_RAYS = int(WINDOW_WIDTH/RES)
    DISTANCE_TO_PROJECTION_PLANE = int((WINDOW_WIDTH / math.tan(FOV)))


    def __init__(self, player, game_map):
        self.rays = []
        self.player = player
        self.map = game_map

    def cast_rays(self):
        initial_angle = self.player.view_angle - (FOV/2)
        delta_angle = FOV / self.TOTAL_RAYS
        self.rays.clear()
        for i in range(self.TOTAL_RAYS):
            self.rays.append(Ray(initial_angle, self.player, self.map))
            initial_angle += delta_angle

    def render(self, screen):
        self.cast_rays()
        i = 0

        draw_begin = 0
        draw_end = (WINDOW_HEIGHT / 2) + 50

        pygame.draw.rect(screen, SKY_COLOR, (0, 0, WINDOW_WIDTH,  draw_end))
        pygame.draw.rect(screen, FLOOR_COLOR, (0, draw_end, WINDOW_WIDTH,  WINDOW_HEIGHT))

        for ray in self.rays:
            ray.render(screen)
            line_height = (WALL_HEIGHT / ray.hit_distance) * self.DISTANCE_TO_PROJECTION_PLANE
            draw_begin = (WINDOW_HEIGHT / 2) - (line_height / 2)
            draw_end = line_height

            pygame.draw.rect(screen, ray.color, (i*RES, draw_begin, RES, draw_end))
            i += 1





