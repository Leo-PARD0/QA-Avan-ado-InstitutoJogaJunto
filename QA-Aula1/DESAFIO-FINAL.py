import json # importa o formato de dados JSON

with open ('clientes.json', 'r') as clientes: # abre o arquivo na pasta que contém os dados do clientes. Usando with não preciso fazer open para depois fazer close no arquivo
    clientes = json.load(clientes) # crio uma variável para armazenar os dados do json

for id, cliente_data in clientes.items(): # inicio do loop para criar as mensagens

    nome = cliente_data["nome"]
    sobrenome = cliente_data["sobrenome"]
    mes = cliente_data["mes"]
    real = float(cliente_data["valor"])

    valor = int(real * 10) 
    # A variável float é interpretada como "x" * 2 elevado a y. 
    # Isso se chama notação cientifica binária e não é capaz de representar todos os valores decimais. 
    # Um exemplo é 0,1. 
    # Para maior precisão usar integrais

    print(f"Para o {id}: {nome}")
    print(f"Nome {nome} {sobrenome}")
    print(f"Mês da compra: {mes}")
    print(f"Valor: R$ {real: .2f}" )

    desconto = int(valor / 5000)

    if desconto > 30:
        desconto = 30

    if desconto >= 1:
        valor_real = str(f"{real}")
        valor_rea = valor_real.replace(".",",")
        msg = str(f"Olá, {nome} {sobrenome}. Em {mes} você realizou uma compra no valor de R$ {valor_real.replace(".",",")} e ganhou um cupom de desconto de {desconto}% em sua próxima compra. Use o cupom {nome}É{desconto}.")
        print(msg)
    else:
        print("Sem cupom")