import pygame
import GameManagement.SceneManager as SceneManager
from GameManagement.Exceptions import *


class GameRoot:
    def __init__(self, screen_dimension: tuple[int, int], default_background_color: tuple[int, int, int]):
        self.display: pygame.Surface = pygame.display.set_mode(screen_dimension)
        self.scenes: list[SceneManager.Scene] = []
        self.background: tuple[int, int, int] = default_background_color

    def register(self, scene: SceneManager.Scene, index=-1):
        if index < 0:
            self.scenes.append(scene)
        else:
            self.scenes.insert(index, scene)

    def mainloop(self):
        done = False
        if len(self.scenes) == 0:
            raise NoAvailableSceneException()
        cur_scene: SceneManager.Scene = self.scenes[0]

        while not done:
            # ___START___
            cur_scene.start_of_frame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            # ___________

            # ___MAIN UPDATE___
            cur_scene.update()
            # _________________

            # __ BLIT THINGS ON THE SCREEN __
            self.display.fill(self.background)
            cur_scene.blit_objects(self.display)  # TMPPP
            pygame.display.update()


