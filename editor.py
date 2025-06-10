import pygame
import sys

from scripts.utils import load_images
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0


class Editor:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Editor")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface(
            (320, 240)
        )  # display here is half the resolution....

        self.clock = pygame.time.Clock()

        self.assets = {
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "stone": load_images("tiles/stone"),
        }
        # print(self.assets)

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

    def run(self):

        while True:
            self.display.fill((0, 0, 0))

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
                        self.movement[1] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[1] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            self.screen.blit(
                pygame.transform.scale(
                    self.display, self.screen.get_size()), (0, 0)
            )
            # self.screen.blit(textSurfaceObj, textRectObj)

            pygame.display.update()
            self.clock.tick(60)


Editor().run()
