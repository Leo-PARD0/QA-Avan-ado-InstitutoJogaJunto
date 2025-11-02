from faker import Faker
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

