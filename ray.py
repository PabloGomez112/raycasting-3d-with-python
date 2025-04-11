import math
import pygame
from vector_utils import Vector2
from vector_utils import distance
from utils import normalize_angle
from settings import *
from map import Map


class Ray:
    player = None
    game_map = None

    def __init__(self, angle, player, game_map):
        """
        :param angle: The angle relative to the player in radians
        :param player: The player object
        """
        self.ray_angle = normalize_angle(angle)
        self.player = player
        self.hit_position = Vector2(0, 0)
        self.already_hit = False

        self.looking_up = False
        self.looking_down = False
        self.looking_left = False
        self.looking_right = False
        self.game_map = game_map
        self.hit_distance = 0
        self.color = (255, 255, 255)

    def update_look_direction(self):
        self.looking_up = not (0 <= self.ray_angle <= math.pi)
        self.looking_down = not self.looking_down
        self.looking_left = (math.pi / 2 <= self.ray_angle <= 3 * math.pi / 2)
        self.looking_right = not self.looking_left

    def cast(self):
        player_x, player_y = self.player.get_position().unpack()
        self.update_look_direction()

        angle_tan = math.tan(self.ray_angle)

        if self.looking_up:
            cell_y = (player_y // TILE_SIZE) * TILE_SIZE - 0.0001
        else:
            cell_y = (player_y // TILE_SIZE) * TILE_SIZE + TILE_SIZE

        x = ((cell_y - player_y) / angle_tan + player_x)
        y = cell_y

        delta_y = -TILE_SIZE if self.looking_up else TILE_SIZE
        delta_x = delta_y / angle_tan

        game_map = self.game_map
        game_map: Map

        vertical_wall = False
        horizontal_wall = False

        while (0 <= x <= WINDOW_WIDTH) and (0 <= y <= WINDOW_HEIGHT):
            if game_map.has_wall_at(x, y):
                self.already_hit = True
                horizontal_wall = True
                break
            else:
                x += delta_x
                y += delta_y

        horizontal_hit = Vector2(x, y)

        cell_x = (player_x // TILE_SIZE) * TILE_SIZE - 0.0001 if self.looking_left \
            else (player_x // TILE_SIZE) * TILE_SIZE + TILE_SIZE
        y = angle_tan * (cell_x - player_x) + player_y

        delta_x = TILE_SIZE if self.looking_right else -TILE_SIZE
        delta_y = delta_x * angle_tan

        x = cell_x

        while (0 <= x <= WINDOW_WIDTH) and (0 <= y <= WINDOW_HEIGHT):
            if game_map.has_wall_at(x, y):
                self.already_hit = True
                vertical_wall = True
                break
            else:
                x += delta_x
                y += delta_y

        vertical_hit = Vector2(x, y)

        view_angle = self.player.view_angle - self.ray_angle
        modified_cos = view_angle * math.cos(view_angle)

        if horizontal_wall:
            horizontal_distance = distance(self.player.get_position(), horizontal_hit)
        else:
            horizontal_distance = math.inf

        if vertical_wall:
            vertical_distance = distance(self.player.get_position(), vertical_hit)
        else:
            vertical_distance = math.inf

        if horizontal_distance < vertical_distance:
            self.hit_position = horizontal_hit
            self.hit_distance = horizontal_distance
            self.color = (10 ,50, 50)
        else:
            self.hit_position = vertical_hit
            self.hit_distance = vertical_distance
            self.color = (255, 255, 255)

        self.hit_distance *= math.cos(self.player.view_angle - self.ray_angle)

    def render(self, screen):
        player_position = self.player.get_position()
        player_position: Vector2
        self.cast()

        """ pygame.draw.line(screen, (255, 0, 0), (player_position.get_x(), player_position.get_y()),
                         (player_position.get_x() + math.cos(self.ray_angle) * 60,
                          player_position.get_y() + math.sin(self.ray_angle) * 60), width=2
        """
        """pygame.draw.line(screen, (255, 0, 0), (player_position.get_x(), player_position.get_y()),
                         (self.hit_position.get_x(), self.hit_position.get_y()), width=2)"""
