"""
# Descrição

Arquivo relacionado à atividade 8.15 da parte 1.

# Resposta

Ao invés disso, vou utilizar a função do arquivo city_names.py, do exercício 
8.6.
"""

from city_names import city_country

def main() -> None:
    vitoria = city_country("Vitória", "Brasil")

    print(vitoria)

if __name__ == "__main__":
    main()