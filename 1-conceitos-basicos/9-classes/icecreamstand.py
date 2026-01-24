"""
# Descrição

Arquivo relacionado à atividade 9.6 da parte 1.
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


class IceCreamStand(Restaurant):
    def __init__(self, flavors: list[str]) -> None:
        super().__init__("IceCreamStand", "Ice cream")
        self.flavors = flavors
    
    def get_flavors(self) -> list[str]:
        return self.flavors


def main() -> None:
    sor = IceCreamStand(["Baunilha", "Chocolate"])

    print(sor.get_flavors())


if __name__ == "__main__":
    main()