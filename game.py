# -*- coding: utf-8 -*-
# https://youtu.be/2gABYM5M0ww?t=6403
# https://github.com/practical-tutorials/project-based-learning?tab=readme-ov-file
# Explore
import pygame
import sys

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player

from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

# set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface(
            (320, 240)
        )  # display here is half the resolution....

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "stone": load_images("tiles/stone"),
            "player": load_image("entities/player.png"),
            "background": load_image('background.png'),
            "clouds": load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }
        # print(self.assets)

        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = Player(self, (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
        self.tilemap.load('map.json')

        self.scroll = [0, 0]

        # data\images\entities\player.png
        # ok
        # data\images\tiles\decor

    def run(self):

        while True:
            self.display.blit(self.assets['background'], (0, 0))
            self.scroll[0] += (self.player.rect().centerx -
                               self.display.get_width()/2 - self.scroll[0])/30
            self.scroll[1] += (self.player.rect().centery -
                               self.display.get_width()/2 - self.scroll[1])/30

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset=self.scroll)

            self.player.update(
                self.tilemap, (self.movement[1] - self.movement[0], 0))

            self.player.render(self.display, offset=render_scroll)

            # print(self.tilemap.tiles_around(self.player.pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[-0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        if self.player.velocity[1] >= 0 and self.player.velocity[1] <= 0.5:
                            pass
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(
                pygame.transform.scale(
                    self.display, self.screen.get_size()), (0, 0)
            )
            # self.screen.blit(textSurfaceObj, textRectObj)

            pygame.display.update()
            self.clock.tick(60)


Game().run()
# sadfsdf


def main() -> None:
    pass


if __name__ == '__main__':
    main()
