import json # importa o formato de dados JSON

with open ('clientes.json', 'r') as clientes: # abre o arquivo na pasta que contém os dados do clientes. Usando with não preciso fazer open para depois fazer close no arquivo
    data = json.load(clientes) # crio uma variável para armazenar os dados do json

for id, cliente_data in data.items(): # inicio um loop para criar as mensagens

    nome = cliente_data["nome"]
    sobrenome = cliente_data["sobrenome"]
    mes = cliente_data["mes"]
    real = float(cliente_data["valor"])

    valor = int(real * 100)

    print(f"Para o {id}: {nome}")
    print(f"Nome {nome} {sobrenome}")
    print(f"Mês da compra: {mes}")
    print(f"Valor: R$ {real}" )

    desconto = int(valor / 5000)

    if desconto > 30:
        desconto = 30

    if desconto >= 1:
        msg = str(f"Olá, {nome} {sobrenome}. Em {mes} você realizou uma compra no valor de R$ {real} e ganhou um cupom de desconto de {desconto}% em sua próxima compra. Use o cupom {nome}é{desconto}.")
        print(msg)
    else:
        print("Sem cupom")