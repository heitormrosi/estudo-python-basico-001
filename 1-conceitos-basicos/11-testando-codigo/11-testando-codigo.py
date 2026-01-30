"""
# Descrição

Arquivo para testar código do capítulo
"""

import unittest

def retorna_nome() -> str:
    return "Heitor"


class TestRetornaNome(unittest.TestCase):
    def test_retorno(self) -> None:
        nome = retorna_nome()
        self.assertEqual(nome, "Heitor")


if __name__ == "__main__":
    unittest.main()
