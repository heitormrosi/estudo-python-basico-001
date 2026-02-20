import pygame as pg
from settings import Settings

class Bullet(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, settings: Settings) -> None:
        super().__init__()
        
        self.settings = settings

        self.image = pg.Surface(self.settings.bullet_size)
        self.image.fill(self.settings.bullet_color)

        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
    
    def update(self) -> None:
        self.rect.x += self.settings.bullet_speed
    