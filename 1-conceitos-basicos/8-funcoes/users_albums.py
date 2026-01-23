"""
# Descrição

Arquivo relacionado à atividade 8.8 da parte 1.
"""

def make_album(artista: str, album: str, num_faixas: int = None) -> dict:
    obj_album = {}

    obj_album.setdefault("artista", artista)
    obj_album.setdefault("album", album)

    if num_faixas:
        obj_album.setdefault("num_faixas", num_faixas)
    
    return obj_album


def main() -> None:
    while True:
        artista = input("Insira o artista (q para sair): ")

        if artista == "q":
            break

        album = input("Insira o album (q para sair): ")

        if album == "q":
            break
        
        print(make_album(artista, album))




if __name__ == "__main__":
    main()