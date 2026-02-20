import pygame as pg
from settings import Settings
from bullet import Bullet

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
        
        self.bullets = pg.sprite.Group()
    
    def shoot(self) -> None:
        if len(self.bullets) < 5:
            self.bullets.add(Bullet(
                self.image_rect.centerx, 
                self.image_rect.centery, self.settings))
    
    def update(self) -> None:
        if self.moving_top and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= self.settings.spaceship_speed
        
        if self.moving_bottom \
                and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += self.settings.spaceship_speed
        
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_rect.right:
                self.bullets.remove(bullet)
                del bullet
    
    def render(self) -> None:
        self.screen.blit(self.image, self.image_rect)
        
        self.bullets.update()
        self.bullets.draw(self.screen)
