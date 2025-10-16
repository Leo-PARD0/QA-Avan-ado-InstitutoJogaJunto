nome = input("Digite seu nome: ")

soma = 0
quantidade = int(input("Digite a quantidade de notas: "))

for i in range(1, quantidade+1):
    nota_data = str(input(f"Digite a {i}ª nota: "))
    nota = float(nota_data.replace(",","."))
    soma += nota

media = soma / quantidade

m = str(f"{media: .1f}")

print(f"Olá, {nome}! Sua média é: {m.replace(".",",")}")