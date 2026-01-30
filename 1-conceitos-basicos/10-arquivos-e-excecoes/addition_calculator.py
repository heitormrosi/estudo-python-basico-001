"""
# Descrição

Arquivo relacionado à atividade 10.7 da parte 1.
"""

def main() -> None:
    print("Adicionarei os dois números informados.")
    
    while True:
        try:
            print("Forneça um número (q para sair).")
            n1 = input("> ")
            if n1.lower() == "q":
                break
            n1 = int(n1)

            print("Forneça outro número (q para sair).")
            n2 = input("> ")
            if n2.lower() == "q":
                break
            n2 = int(n2)
        except ValueError:
            # Na verdade, não é TypeError, é ValueError.
            print("O valor fornecido é inválido. Tente novamente.")
        else:
            print(f"A soma dos números é {n1+n2}")


if __name__ == "__main__":
    main()