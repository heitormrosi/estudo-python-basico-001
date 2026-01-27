"""
# Descrição

Arquivo relacionado à atividade 9.14 da parte 1.
"""

from random import randint

class Dice:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
    
    def roll_dice(self) -> None:
        print(randint(1, self.sides))


def main() -> None:
    d6 = Dice()
    d10 = Dice(10)
    d20 = Dice(20)

    for _ in range(10):
        d6.roll_dice()
    
    for _ in range(10):
        d10.roll_dice()
    
    for _ in range(10):
        d20.roll_dice()


if __name__ == "__main__":
    main()