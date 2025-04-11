import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

TICKS_FOR_SECOND = 60

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_map = Map()
player = Player(game_map.get_spawn_position())
ray_caster = Raycaster(player, game_map)

clock = pygame.time.Clock()

def update_game():
    player.update()

def render_game():
    #game_map.render(screen)
    player.render(screen)
    ray_caster.render(screen)

while True:
    clock.tick(TICKS_FOR_SECOND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    render_game()
    update_game()
    pygame.display.update()


