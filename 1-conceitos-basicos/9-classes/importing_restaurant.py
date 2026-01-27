"""
# Descrição

Arquivo relacionado à atividade 9.10 da parte 1.
"""

from restaurant import Restaurant

def main() -> None:
    res = Restaurant("Burguer King", "Hambúrguer")

    res.describe_restaurant()


if __name__ == "__main__":
    main()