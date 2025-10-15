nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}, você tem {idade} anos, certo? ")
bool = input("Digite [y/n]: ")

if bool == 'y' or bool == 'Y':
    print("Entendi!")
    if idade < 18:
        espera = 18 - idade
        print(f"{nome}, você é menor de idade! não pode fazer o curso. Faltam {espera} anos.")
    else:
        print(f"Seja bem vindo ao curso avançado de QA, {nome}!")
elif bool == 'n' or bool == 'N':
    idade = int(input("Digite sua idade correta: "))
    print("Idade atualizada com sucesso!")
    if idade < 18:
        espera = 18 - idade
        print(f"{nome}, você é menor de idade! não pode fazer o curso. Faltam {espera} anos.")
    else:
        print(f"Seja bem vindo ao curso avançado de QA, {nome}!")
else:
    print("Perdão, não entendi. Pode repetir o processo?")