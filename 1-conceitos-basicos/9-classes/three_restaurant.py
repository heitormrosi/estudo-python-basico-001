"""
# Descrição

Arquivo relacionado à atividade 9.2 da parte 1.
"""

class Restaurant:
    def __init__(
            self,
            restaurant_name: str,
            cuisine_type: str
            ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) -> None:
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self) -> None:
        print("O restaurante está aberto agora!")


def main() -> None:
    r1 = Restaurant("Restaurante 1", "Sanduíche")
    r2 = Restaurant("Restaurante 2", "Kebab")
    r3 = Restaurant("Restaurante 3", "Lasanha")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()


if __name__ == "__main__":
    main()