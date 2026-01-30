"""
# Descrição

Arquivo relacionado à atividade 10.13 da parte 1.
"""

import json

def get_stored_username(): 
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'

    try: 
        with open(filename) as f_obj: 
            username = json.load(f_obj) 
    except FileNotFoundError: 
        return None
    else: 
        return username


def get_new_username(): 
    """Pede um novo nome de usuário."""
    username = input("What is your name? ") 
    filename = 'username.json'

    with open(filename, 'w') as f_obj: 
        json.dump(username, f_obj)

    return username


def greet_user(): 
    """Saúda o usuário pelo nome."""
    username = get_stored_username() 
    
    if username: 
        print(f"Is your name {username}?")
        response = input("Yes or no > ").lower()

        if response == "yes": 
            print("Welcome back, " + username + "!") 
            return

    username = get_new_username() 

    print("We'll remember you when you come back, " + username + "!")


def main() -> None:
    greet_user()


if __name__ == "__main__":
    main()