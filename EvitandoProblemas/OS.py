'''
Vamos explorar o poder da biblioteca OS! Prepare-se para mergulhar no mundo da interação entre o Python e o seu sistema operacional. Vamos aprender a usar a biblioteca OS em conjunto com funções nativas do Python para criar algo.

O desafio é o seguinte: você vai criar uma lista de dados e, usando a biblioteca OS, interagir com o seu sistema operacional. Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.
'''
import os
import json

dados = {}
continuar = True
while continuar == True: # loop para salvar os dados no dicionário
    nome = input('Digite um nome: ')
    url = input('Digite um o link do seu perfil no Linkedin: ')
    dados[nome] = url
    resposta = input('Adicionar uma nova conexão?[s/n] ').lower()
    if resposta != 's':
        continuar = False

output_dir = 'output' # pasta de saída
os.makedirs(output_dir, exist_ok=True) # verifica a pasta output e se não existe, cria

arquivo = input('Digite o nome do arquivo: ').strip()
if not arquivo.endswith('.json'):
    arquivo += '.json'

caminho_arquivo = os.path.join(output_dir, arquivo)

with open(caminho_arquivo, 'w') as arq: # escreve os arquivos com o argumento dado em arq.write
    json.dump(dados, arq, indent=4)