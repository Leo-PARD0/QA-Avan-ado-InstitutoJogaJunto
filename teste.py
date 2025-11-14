import requests
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def vasculhar_endpoint(endpoints):
    responses = requests.get(endpoints)
    responses.raise_for_status()
    return responses.json()


#books = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/books/')

""" books_df = pd.DataFrame(books)
books_df.to_csv('books.csv', index=False, encoding='utf-8')

books_from_csv = pd.read_csv('books.csv') """
#print(books_from_csv)



books = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/books/')
authors = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/authors/')

print(pd.DataFrame(books))

for item in authors:
    id_procurado = []
    if item['name'] == 'Ellen Salvador':
        #id_procurado = item['id']
        id_procurado.append(item['id'])
        print(pd.DataFrame(id_procurado))
    else: id_procurado = None

responses = vasculhar_endpoint('http://apilivro.jogajuntoinstituto.org/books/')


for item in responses:
    if item['author'] in id_procurado:
        print(f"Livro encontrado: {item['title']}")
        print(f'Autor é: {item["author"]}')

#print(books)