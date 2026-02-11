import pygame as pg
import sys

def main() -> None:
    screen = pg.display.set_mode((600, 600))
    pg.display.set_caption("Capturando teclas.")
    
    # Para limitar a renderização.
    clock = pg.time.Clock()

    # Não precisa renderizar a tela várias vezes.
    # Plano de fundo amarelo.
    screen.fill((255, 255, 0))
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                print(event.key)
        
        clock.tick(10)


if __name__ == "__main__":
    main()