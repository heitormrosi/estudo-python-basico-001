import pygame as pg
from settings import Settings
from element import Element

class Spaceship(Element):
    """ Elemento da espaçonave no jogo. """

    def __init__(self, parent_surface: pg.Surface, settings: Settings) -> None:
        self.settings = settings
        
        # Redimensiona a imagem importada para o tamanho das configurações.
        self.image = pg.transform.scale(
            pg.image.load(self.settings.spaceship_file),
            self.settings.spaceship_size
        )

        super().__init__(
            parent_surface,
            self.image
        )
        
        # Redimensiona o retângulo para o tamanho da nave e 
        # desenha a superfície da nave centralizada no retângulo.
        # Foi necessário desenhar uma superfície maior que o retângulo para 
        # evitar deformação na imagem.
        self.rect.width = int(self.rect.height / 1.5)
        self.rect.center = self.parent_rect.center
        self.area = pg.Rect(
            (self.surface.get_width() - self.rect.width)//2, 
            0, self.rect.width, self.rect.height)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def events(self, event: pg.event.Event) -> None:
        # Lida com a detecção de comandos para 
        # a movimentação da espaçonave.
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                self.moving_right = True
            elif event.key == pg.K_a:
                self.moving_left = True
            elif event.key == pg.K_w:
                self.moving_up = True
            elif event.key == pg.K_s:
                self.moving_down = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                self.moving_right = False
            elif event.key == pg.K_a:
                self.moving_left = False
            elif event.key == pg.K_w:
                self.moving_up = False
            elif event.key == pg.K_s:
                self.moving_down = False
    
    def update(self) -> None:
        # Lida com a movimentação da nave e com seus limites dentro 
        # da janela.
        if self.moving_right and self.rect.right < self.parent_rect.right:
            self.rect.x += self.settings.spaceship_speed
        
        if self.moving_left and self.rect.left > self.parent_rect.left:
            self.rect.x -= self.settings.spaceship_speed 
        
        if self.moving_up and self.rect.top > self.parent_rect.top:
            self.rect.y -= self.settings.spaceship_speed
        
        if self.moving_down and self.rect.bottom < self.parent_rect.bottom:
            self.rect.y += self.settings.spaceship_speed
        