"""
# Descrição

Arquivo relacionado à atividade 8.16 da parte 1.

# Resposta

O arquivo separado será [separate_function.py](./separate_function.py).
"""

import separate_function
from separate_function import mostrar_sanduiche
from separate_function import mostrar_sanduiche as ms
import separate_function as sf
from separate_function import *


def main() -> None:
    ms("Pão", "Mortadela", "Mortadela", "Mortadela", "Mortadela", "Mortadela")


if __name__ == "__main__":
    main()