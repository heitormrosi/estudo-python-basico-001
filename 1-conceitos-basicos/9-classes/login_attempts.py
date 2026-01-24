"""
# Descrição

Arquivo relacionado à atividade 9.5 da parte 1.
"""

class User:
    def __init__(
            self, 
            first_name: str, 
            last_name: str, 
            age: int,
            login_attempts: int = 0
            ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts
    
    def greet_user(self) -> None:
        print(f"Olá, {self.first_name} {self.last_name}!")
    
    def describe_user(self) -> None:
        print(f"Nome do usuário: {self.first_name} {self.last_name}")
        print(f"Idade: {self.age}")
    
    def increment_login_attempts(self) -> None:
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0


def main() -> None:
    heitor = User("Heitor", "YT", 18)
    message = "Quantidade de logins"

    heitor.greet_user()
    heitor.describe_user()

    heitor.increment_login_attempts()
    heitor.increment_login_attempts()
    heitor.increment_login_attempts()

    print(f"{message}: {heitor.login_attempts}")

    heitor.reset_login_attempts()

    print(f"{message}: {heitor.login_attempts}")


if __name__ == "__main__":
    main()