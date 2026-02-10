from settings import Settings
from window import Window
from spaceship import Spaceship

class Rocket:
    """ Jogo de foguete voando. """

    def __init__(self) -> None:
        self.settings = Settings()
        self.window = Window(self.settings)
        self.spaceship = Spaceship(self.window.window, self.settings)
        
        self.window.add_events(self.spaceship)

        self.window.add_element(self.spaceship)
    
    def run(self) -> None:
        self.window.run()


def main() -> None:
    rocket = Rocket()
    rocket.run()


if __name__ == "__main__":
    main()