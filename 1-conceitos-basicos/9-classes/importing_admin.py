"""
# Descrição

Arquivo relacionado à atividade 9.11 da parte 1.
"""

from privileges import Admin

def main() -> None:
    adm = Admin()

    adm.show_privileges()


if __name__ == "__main__":
    main()