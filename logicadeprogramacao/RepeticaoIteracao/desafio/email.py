user = {
    "nome": "placeholder",
    "email": "email@placeholder"
} # dicinoário para cada aluno do instituto joga junto

user['nome'] = input("Digite seu nome: ")
user['email'] = input("Digite seu email: ")

for key, value in user.items(): # para chave e valor em itens do dicionário.
    dominio = user["email"].split("@", 1) # dividir o valor por "@"
    if dominio[1] == "jogajuntoinstituto.org": # se o valor dividido por "@" for igual a "@jogajuntoinstituto.org"
        print(f"DEBUG: {dominio}")
        print(f"{user['nome']}, o email tem o domínio correto.")
    else:
        print(f"DEBUG: {dominio}")
        print(f"{user['nome']}, o email não tem o domínio correto.")