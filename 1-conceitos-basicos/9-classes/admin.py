"""
# Descrição

Arquivo relacionado à atividade 9.7 da parte 1.
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


class Admin(User):
    def __init__(self) -> None:
        super().__init__("Admin", "", 0)
        self.privileges = [
            "can ban user",
            "can add post"
        ]
    
    def show_privileges(self) -> None:
        print(" Privilégios do Admin ".center(30, "="))
        for privilege in self.privileges:
            print(privilege)


def main() -> None:
    admin = Admin()

    admin.show_privileges()


if __name__ == "__main__":
    main()