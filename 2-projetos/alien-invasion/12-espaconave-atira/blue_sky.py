"""
# Descrição

Arquivo relacionado à atividade 12.1 da parte 2.
"""

import sys

import pygame as pg

def main() -> None:
    pg.init()
    
    screen = pg.display.set_mode((600, 600))
    
    pg.display.set_caption("Céu Azul")
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.fill((0, 0, 255))
        
        pg.display.flip()


if __name__ == "__main__":
    main()