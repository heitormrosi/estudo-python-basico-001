"""
# Descrição

Arquivo relacionado à atividade 9.3 da parte 1.
"""

class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def greet_user(self) -> None:
        print(f"Olá, {self.first_name} {self.last_name}!")
    
    def describe_user(self) -> None:
        print(f"Nome do usuário: {self.first_name} {self.last_name}")
        print(f"Idade: {self.age}")


def main() -> None:
    heitor = User("Heitor", "YT", 18)
    carlos = User("Carlos", "Perim", 99)
    # É óbvio que essa idade não existe '-'
    joao = User("Pedro", "Sampaio", -10)

    heitor.greet_user()
    heitor.describe_user()

    carlos.greet_user()
    carlos.describe_user()

    joao.greet_user()
    joao.describe_user()


if __name__ == "__main__":
    main()