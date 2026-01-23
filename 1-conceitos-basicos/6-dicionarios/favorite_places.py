"""
# Descrição

Arquivo relacionado à atividade 6.9 da parte 1.
"""

OUTPUT_SIZE = 30

favorite_places = {
    "Heitor": [
        "Paço Imperial", "Museu Imperial", "Assembleia Legislativa"
    ],
    "Fulano": [
        "Museu", "Monte Everest", "Muralha da China"
    ],
    "Beltrano": [
        "Terminal de ônibus", "Cristo Redentor", "Coliseu"
    ]
}

for nome, lugares in favorite_places.items():
    print(f"+{"= Lugares favoritos de =".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"|{nome.center(OUTPUT_SIZE, " ")}|")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    for lugar in lugares:
        print(f"|{lugar.center(OUTPUT_SIZE, " ")}|")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print()