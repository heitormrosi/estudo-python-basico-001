"""
# Descrição

Arquivo relacionado à atividade 6.12 da parte 1.
"""

import textwrap

OUTPUT_SIZE = 30

cities = {
    "Tóquio": {
        "country": "Japão",
        "population": "37.4 milhões",
        "fact": "É a área metropolitana mais populosa do mundo."
    },
    "Paris": {
        "country": "França",
        "population": "2.1 milhões",
        "fact": "É conhecida como a \"Cidade Luz\" devido ao seu papel durante o Iluminismo."
    },
    "Rio de Janeiro": {
        "country": "Brasil",
        "population": "6.7 milhões",
        "fact": "Abriga o Cristo Redentor, uma das Sete Maravilhas do Mundo Moderno."
    },
    "Cairo": {
        "country": "Egito",
        "population": "10.1 milhões",
        "fact": "É a maior cidade do mundo árabe e fica próxima às Pirâmides de Gizé."
    },
    "Londres": {
        "country": "Reino Unido",
        "population": "8.9 milhões",
        "fact": "O metrô de Londres, o \"Tube\", é o sistema de transporte subterrâneo mais antigo do mundo."
    }
}

for cidade, informacoes in cities.items():
    print(f"+{"= Informações de cidade =".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE)}|")
    print(f"|{cidade.title().center(OUTPUT_SIZE)}|")
    print(f"|{"   ".center(OUTPUT_SIZE)}|")
    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE)}|")

    for titulo, informacao in informacoes.items():
        if len(informacao) > 10:
            tmp = textwrap.wrap(informacao, width=OUTPUT_SIZE-7)
            print(f"|{f" {titulo.capitalize()}: {tmp.pop(0)}".ljust(OUTPUT_SIZE)}|")
            for inf in tmp:
                print(f"| {f"{inf}".ljust(OUTPUT_SIZE-2)} |")
        else:
            print(f"|{f" {titulo.capitalize()}: {informacao}".ljust(OUTPUT_SIZE)}|")

        print(f"|{"   ".center(OUTPUT_SIZE)}|")

    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print()