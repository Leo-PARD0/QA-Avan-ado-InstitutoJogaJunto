def saudacao(nome):
    if nome == 'leo':
        print('Eae, Leo!')
    else:
        print(f'Olá, visitante.')

name = input('Digite seu nome: ').lower()
saudacao(name)