"""
# Descrição

Arquivo relacionado à atividade 8.13 da parte 1.
"""

def build_profile(nome: str, sobrenome: str, **outros_dados) -> dict:
    profile = {}

    profile.update({
        "nome": nome,
        "sobrenome": sobrenome
    })

    profile.update(outros_dados)

    return profile


def main() -> None:
    perfil = build_profile(
        "Heitor", 
        "Musk", 
        violao=True, 
        cybersecurity=True,
        caneta_na_mao="BIC Crystal .8mm"
    )

    print(perfil)


if __name__ == "__main__":
    main()