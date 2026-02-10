import pygame as pg
from settings import Settings
from element import Element

class Window:
    """ Janela personalizada do Pygame. """
    
    def __init__(self, settings: Settings) -> None:
        pg.init()
        
        # Uso do padrão de objeto observador para renderizar e atualizar 
        # os elementos passados.
        self.elements: list[Element] = []
        self.events: list[Element] = []

        self.settings = settings

        self.window = pg.display.set_mode(self.settings.window_size)
        pg.display.set_caption(self.settings.window_title)
        
        self.clock = pg.time.Clock()

        self.running: bool = False
    
    def add_element(self, element: Element) -> None:
        self.elements.append(element)
    
    def add_events(self, element: Element) -> None:
        self.events.append(element)
    
    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.running = False
            
            for element in self.events:
                element.events(event)
    
    def run(self) -> None:
        self.running = True
        
        while self.running:
            self.check_events()
            self.render()
    
    def render(self) -> None:
        self.window.fill(self.settings.window_bg_color)
        
        for element in self.elements:
            element.update()
            self.window.blit(element.surface, element.rect, area=element.area)

        pg.display.flip()
        self.clock.tick(self.settings.fps)