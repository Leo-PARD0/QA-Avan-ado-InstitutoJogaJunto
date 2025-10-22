nome_pet = str(input("Qual o nome do seu pet? "))
idadeH = int(input("Quantos anos seu cachorro tem? "))
idadeC = int(idadeH*7)

porte = input("Qual o porte do seu cachorro: Grande (g), Médio (m) ou Pequeno (p)? ").lower()

periodo = int(input("A quantos meses seu cachorro é atendido? "))
banho = int(input("Quantos banhos ele tomou nesse período? "))

debug = str(f"nome do pet: {nome_pet}, idade do pet: {idadeH}, idade em anos de cachorro: {idadeC}, porte do cachorro {porte}, o período digitado é: {periodo}, a quantidade de banhos tomados: {banho}")
print(debug)

custo = 00.00
valor = 00.00

match porte:
    case "g":
        valor = 75.00
        custo = 20.00
    case "m":
        valor = 60.00
        custo = 15.00
    case "p":
        valor = 50.00
        custo = 05.00
    case _:
        print ("Irmão, não entendi, tente escrever do jeito que está escrito.")

lucro = valor - custo
lucro_periodo = lucro * periodo

mensagem = f"Olá, {nome_pet} tem {idadeC} anos em idade de cachorro e nos últimos {periodo} meses ele gerou: R$ {lucro_periodo}"

print(mensagem)