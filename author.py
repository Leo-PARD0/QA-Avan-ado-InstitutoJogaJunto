import requests # importa a biblioteca requests para acessar o site
import pandas as pd # importa pandas para visualizar melhor no terminal

pd.set_option('display.max_rows', None) # configura o pandas para mostrar todas as linhas
pd.set_option('display.max_columns', None) # configura o pandas para mostrar todas as colunas


def vasculhar_endpoint(endpoints): # função que acessa o endpoint e retorna um json com os dados
    responses = requests.get(endpoints)
    responses.raise_for_status()
    return responses.json()


books = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/books/') # Acessa os livros e salva na variável books
authors = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/authors/') # Acessa os autores e salva na variável authors

""" 
    O endpoint books retorna uma lista mostrando título, descrição, autor e genero. Contúdo, autor e genero só pode ser encontrado por id.

    Para fazer uma busca por nome, devemos buscar o id no endpoint author, assim, guardamos o(s) ID(s), para buscar o livro no endpoint books
"""
nome = input("Qual o nome do autor que você está buscando? ") # perguntamos para o usuário qual o nome a ser buscado no authors
id_procurado = [] # declara a lista de ids, pois o mesmo autor pode ter mais de 1 id
for item in authors: # o endpoint authors retorna uma lista de dicionários, devemos iterar cada dicionário para encontrar a chave 'name' dentro deles
    if nome.lower() in item['name'].lower(): # vasculha se o nome buscado está presente no texto de item['name']. lower() está aqui para fazer a busca completa, independente de maiúsculas e minúsculas
        id_procurado.append(item['id']) # aumenta a lista de ids

print(id_procurado) # imprime os ids do autor procurado

livros = [] # declara a lista de livros para criar uma lista de um único autor
for item in books: # para cada dicionário (item) dentro da lista de dicionários (book)
    if item['author'] in id_procurado: # se o id do autor estiver presente na lista do id procurado
        livros.append(item) # então a lista de livros será atualizada com o livro iterado


print(pd.DataFrame(livros)) # imprime a lista de livros formatada pelo pandas
