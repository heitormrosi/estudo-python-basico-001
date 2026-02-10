class Settings:
    """ Configurações do jogo de foquete voando. """

    def __init__(self) -> None:
        self.window_size = (600, 600)
        self.window_title = "Foguete"
        self.window_bg_color = (0, 0, 0)
        self.fps = 60
        
        self.spaceship_file = "./img/spaceship.png"
        self.spaceship_size = (100, 100)
        self.spaceship_speed = 5