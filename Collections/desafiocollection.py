tupla = ('1','2','3','4','5')
lista = list(tupla)
lista.append('6')
lista.append('7')
lista.pop(6)
lista.pop(0)
print(f"O primeiro valor é: {lista[0]}")
print(f"A quantidade de valores é: {len(lista)}")

dicionario = {"nome":"nome","idade":"idade","profissão":"profissão"}
dicionario['nome'] = input("Qual o seu nome? ")
dicionario['idade'] = input("Qual a sua idade? ")
dicionario['profissão'] = input("Qual a sua profissão? ")
print(f"o nome no dicionário é: {dicionario['nome']}")