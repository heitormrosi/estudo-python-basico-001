"""
# Descrição

Arquivo relacionado à atividade 9.4 da parte 1.
"""

class Restaurant:
    def __init__(
            self,
            restaurant_name: str,
            cuisine_type: str,
            number_served: int = 0
            ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self) -> None:
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self) -> None:
        print("O restaurante está aberto agora!")
    
    def set_number_served(self, number_served: int) -> None:
        self.number_served = number_served
    
    def increment_number_served(self, number_served) -> None:
        self.number_served += number_served


def main() -> None:
    res = Restaurant("Chef Mignon", "Sanduíche")

    message = "Número de clientes atendidos:"

    print(res.restaurant_name)
    print(res.cuisine_type)

    res.describe_restaurant()
    res.open_restaurant()

    print(f"{message} {res.number_served}")

    res.set_number_served(20)
    res.increment_number_served(10)

    print(f"{message} {res.number_served}")


if __name__ == "__main__":
    main()