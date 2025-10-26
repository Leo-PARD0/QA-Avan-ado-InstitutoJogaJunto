nome = str(input("Digite seu nome: "))
print(f"Olá, {nome} vou verificar se você tem idade para dirigir.")
idade = int(input("Digite sua idade em anos: "))

pode = str(f"Com {idade} anos você tem permissão para dirigir!")
minimo = str(f"Com {idade} anos você tem a idade minima para dirigir.")
impedido = str(f"Com {idade} anos você ainda não pode dirigir, espere {18-idade} anos para poder dirigir.")

if (idade > 18):
    print(pode)
elif (idade == 18):
    print(minimo)
else:
    print(impedido)