"""
# Descrição

Arquivo relacionado à atividade 9.1 da parte 1.
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
    res = Restaurant("Chef Mignon", "Sanduíche")

    print(res.restaurant_name)
    print(res.cuisine_type)

    res.describe_restaurant()
    res.open_restaurant()


# Permite utilizar o arquivo como módulo.
if __name__ == "__main__":
    main()