from __future__ import annotations
import typing

import pygame
from GameManagement.Utilities.funcs import do_intersect

if typing.TYPE_CHECKING:
    from GameManagement.SceneManager import Scene
    from GameManagement.Utilities.Objects import GameObject


class BaseComponent:
    def __init__(self):
        pass

    def on_scene_init(self, this: GameObject, scene: Scene):
        pass

    def on_scene_early_update(self, this: GameObject, scene: Scene):
        pass

    def on_scene_update(self, this: GameObject, scene: Scene):
        pass


class CameraComponent(BaseComponent):
    def __init__(self):
        super().__init__()

    @classmethod
    def blit_objects(cls, this: GameObject, scene: Scene, disp: pygame.Surface):
        for obj in scene.gameObjects.values():
            # if not do_intersect(this.rect, obj.rect):
            #     continue

            obj.blit(disp, this.pos)

