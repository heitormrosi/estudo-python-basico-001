"""
# Descrição

Arquivo relacionado à atividade 10.6 da parte 1.
"""

def main() -> None:
    print("Adicionarei os dois números informados.")
    
    try:
        print("Forneça um número.")
        n1 = int(input("> "))
        print("Forneça outro número.")
        n2 = int(input("> "))
    except ValueError:
        # Na verdade, não é TypeError, é ValueError.
        print("O valor fornecido é inválido.")
    else:
        print(f"A soma dos números é {n1+n2}")


if __name__ == "__main__":
    main()