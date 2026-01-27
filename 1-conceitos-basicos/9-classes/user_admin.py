"""
# Descrição

Arquivo relacionado à atividade 9.12 da parte 1.
"""

from user import User

class Privileges:
    def __init__(self) -> None:
        self.privileges = [
            "can ban user",
            "can add post"
        ]
    
    def show_privileges(self) -> None:
        print(" Privilégios ".center(30, "="))
        for privilege in self.privileges:
            print(privilege)


# Se eu não me engano, isso se chama composição em programação orientada a 
# objetos.
class Admin(User):
    def __init__(self) -> None:
        super().__init__("Admin", "", 0)
        self.privileges = Privileges()