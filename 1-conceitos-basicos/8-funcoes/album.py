"""
# Descrição

Arquivo relacionado à atividade 8.7 da parte 1.
"""

def make_album(artista: str, album: str, num_faixas: int = None) -> dict:
    obj_album = {}

    obj_album.setdefault("artista", artista)
    obj_album.setdefault("album", album)

    if num_faixas:
        obj_album.setdefault("num_faixas", num_faixas)
    
    return obj_album


def main() -> None:
    mj_album = make_album("Michael Jackson", "Thriller")
    vm_album = make_album("Vinícios de Moraes", "O Poeta e o Violão")
    lb_album = make_album("Lô Borges", "Clube da Esquina")
    rn_album = make_album("Ren", "Sick Boi", 5)

    print(mj_album)
    print(vm_album)
    print(lb_album)
    print(rn_album)


if __name__ == "__main__":
    main()