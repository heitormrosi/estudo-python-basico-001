"""
# Descrição

Arquivo relacionado à atividade 11.3 da parte 1.
"""

from unittest import TestCase, main

from employee import Employee


class TestEmployee(TestCase):
    def setUp(self) -> None:
        self.nome = "Heitor"
        self.sobrenome = "Sobrenome"
        self.salario_anual = 5_000
        self.employee = Employee(
            self.nome,
            self.sobrenome,
            self.salario_anual
        )
    
    def test_give_default_raise(self) -> None:
        self.employee.give_raise()
        self.salario_anual += 5_000
        self.assertEqual(
            self.employee.salario_anual,
            self.salario_anual
        )
    
    def test_give_custom_raise(self) -> None:
        self.employee.give_raise(10_000)
        self.salario_anual += 10_000
        self.assertEqual(
            self.employee.salario_anual,
            self.salario_anual
        )


if __name__ == "__main__":
    main()