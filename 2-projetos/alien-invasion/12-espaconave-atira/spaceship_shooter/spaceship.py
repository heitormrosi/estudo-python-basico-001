import pygame as pg
from settings import Settings

class Spaceship:
    def __init__(self, screen: pg.Surface, settings: Settings) -> None:
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pg.image.load(self.settings.spaceship_filepath)
        
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = self.screen_rect.centery
        self.image_rect.size = (104, 70)

        self.image = pg.transform.scale(self.image, self.image_rect.size)
        
        self.moving_top = False
        self.moving_bottom = False
    
    def update(self) -> None:
        if self.moving_top and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= self.settings.spaceship_speed
        
        if self.moving_bottom \
                and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += self.settings.spaceship_speed
        
    
    def render(self) -> None:
        self.screen.blit(self.image, self.image_rect)
