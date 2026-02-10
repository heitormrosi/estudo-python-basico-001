import pygame as pg

class Element:
    """ Elemento padrão para renderizar em uma superfície. """

    def __init__(
            self, 
            parent_surface: pg.Surface, 
            surface: pg.Surface
            ) -> None:
        self.parent_surface = parent_surface
        self.parent_rect = parent_surface.get_rect()
        self.surface = surface
        self.rect = surface.get_rect()
        self.area = None

    # As reticências indicam que não são implementados naturalmente.
    def events(self, event: pg.event.Event) -> None: ...
    def update(self) -> None: ...