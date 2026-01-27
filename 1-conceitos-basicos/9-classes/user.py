"""
# Descrição

Arquivo relacionado à atividade 9.12 da parte 1.
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