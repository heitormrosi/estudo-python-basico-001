"""
# Descrição

Arquivo relacionado à atividade 10.5 da parte 1.
"""

def main() -> None:
    while True:
        print("Você gosta de programação?")
        escolha = input("> ")

        print("Por que?")
        motivo = input("> ")

        with open("programming_poll.txt", "a") as fd:
            fd.write(f"{escolha}\n")
            fd.write(f"{motivo}\n")


if __name__ == "__main__":
    main()