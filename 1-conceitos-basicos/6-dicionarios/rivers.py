"""
# Descrição

Arquivo relacionado à atividade 6.5 da parte 1.
"""

rios = {
    "nilo": "egito",
    "amarelo": "china",
    "gangis": "índia"
}

for k, v in rios.items():
    print(f"O rio {k.title()} corre pelo(a) {v.title()}")

for rio in rios.keys():
    print(rio.title())

for pais in rios.values():
    print(pais.title())