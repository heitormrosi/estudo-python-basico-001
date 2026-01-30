"""
# Descrição

Arquivo relacionado à atividade 10.4 da parte 1.
"""

def main() -> None:
    arquivo = "guest_book.txt"

    while True:
        print("Por favor, insira seu nome.")
        print("(quit para sair)")
        nome = input("> ")

        if nome.lower() == "quit":
            break

        print(f"Saudações, {nome}!")

        with open(arquivo, "a") as fd:
            fd.write(f"{nome}\n")


if __name__ == "__main__":
    main()