""" from faker import Faker
import csv
import os

fake = Faker()
fake = Faker("pt-BR")

nome = fake.name()
nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
idade = (2025 - nascimento.year)
cidade = fake.city()
print(nome, cidade, idade)

def lista_pessoas():
    n = int(input("Quantas pessoas deseja gerar? "))
    for i in range(n):
        persona_dict = {
             'nome': fake.first_name() + ' ' + fake.last_name(),
             'email': fake.email(),
             

        }

    
    return persona_dict

lista = lista_pessoas()
print (lista)

output_dir = 'output' # pasta de saída
os.makedirs(output_dir, exist_ok=True) # verifica a pasta output e se não existe, cria

arquivo = input('Digite o nome do arquivo: ').strip()
if not arquivo.endswith('.csv'):
    arquivo += '.csv'

caminho_arquivo = os.path.join(output_dir, arquivo)
with open(caminho_arquivo, mode='w') as csvfile:
        csv_escrito = csv.writer(csvfile)
        csv_escrito.writerow(lista)
 """

from faker import Faker
import pandas as pd
import os
import csv

fake = Faker("pt_BR") # armazena faker em pt br dentro do código

def lista_pessoas(n): # função que cria dicionário de pessoas
    pessoas = [] # esta lista se transformará no dicionário
    for i in range(n):
        pessoa = {
            'Nome' : fake.first_name() + ' ' + fake.last_name(),
            'Cidade' : fake.city(),
            'Idade' : fake.random_int(min=18, max=65)
            }
        pessoas.append(pessoa) # toda pessoa gerada será adicionada a lista pessoas FORA DO LOOP
    return pessoas # retorna pessoas para fora da função

n = int(input('Quantas pessoas deseja gerar? ')) # decide quantas pessoas
pessoas = lista_pessoas(n) # armazena o dicionario fora da função

df = pd.DataFrame(pessoas) # cria uma tabela para ser mostrada no terminal

print(df) # mostra a tabela no terminal

output_dir = 'output' # nome da pasta de saida
os.makedirs(output_dir, exist_ok=True) # os vai criar a pasta output caso o exist_ok retorne true, ou seja, caso seja possível criar

arquivo = input('Digite o nome do arquivo: ').strip() # nome do arquivo final # strip() remove caracteres, no caso de vazio, remove espaços
if not arquivo.endswith == '.csv': # se 'NÃO' o final do arquivo for igual a '.csv', ou seja se o arquivo não acabar com .csv
    arquivo += '.csv' # adiciona a extensão csv ao arquivo

arquivo_dir = os.path.join(output_dir, arquivo) # o caminho do arquivo vai ser a junção de output dir e arquivo.

with open(arquivo_dir, mode='w') as csvfile: # abrindo o caminho do arquivo no modo escrita como a variavel csvfile
    campos = ['Nome', 'Cidade', 'Idade'] # salva os campos de cabeçalho
    escrever_csv = csv.DictWriter(csvfile, fieldnames=campos) # a variavel escrever_csv irá usar csvfile para escrever csv
    escrever_csv.writeheader() # escreve o cabeçalho
    escrever_csv.writerows(pessoas) # a escrita do csv se deve na lista pessoas