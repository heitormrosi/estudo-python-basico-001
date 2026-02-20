import pygame as pg
from settings import Settings
from spaceship import Spaceship

class SpaceshipShooter:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.window = pg.display.set_mode(self.settings.window_size)
        pg.display.set_caption(self.settings.title)
        self.running = False
        
        self.clock = pg.time.Clock()
        
        self.spaceship = Spaceship(self.window, self.settings)
    
    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.spaceship.moving_top = True
                    elif event.key == pg.K_s:
                        self.spaceship.moving_bottom = True 
                    elif event.key == pg.K_SPACE:
                        self.spaceship.shoot()

                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.spaceship.moving_top = False
                    elif event.key == pg.K_s:
                        self.spaceship.moving_bottom = False 

            self.spaceship.update()               

            self.window.fill(self.settings.bg_color)
            
            self.spaceship.render()
            
            pg.display.flip()
            self.clock.tick(self.settings.fps)
    

def main():
    pg.init()

    settings = Settings()
    spaceshipShooter = SpaceshipShooter(settings)
    spaceshipShooter.run()

    pg.quit()


if __name__ == "__main__":
    main()