"""
# Descrição

Arquivo relacionado à atividade 11.3 da parte 1.
"""

class Employee:
    def __init__(
            self, nome: str, sobrenome: str, salario_anual: float) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual
    
    def give_raise(self, aumento: int = 5_000) -> None:
        self.salario_anual += aumento