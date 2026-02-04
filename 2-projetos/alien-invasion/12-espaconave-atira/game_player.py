"""
# Descrição

Arquivo relacionado à atividade 12.2 da parte 2.
"""

import sys

import pygame as pg

def main() -> None:
    pg.init()
    
    screen = pg.display.set_mode((600, 600))
    
    pg.display.set_caption("Master Chief - Halo")
    
    master_chief = pg.image.load("./master-chief.bmp")
    mc_rect = master_chief.get_rect()
    
    mc_rect.center = screen.get_rect().center
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.fill((255, 255, 255))
        screen.blit(master_chief, mc_rect)
        
        pg.display.flip()


if __name__ == "__main__":
    main()