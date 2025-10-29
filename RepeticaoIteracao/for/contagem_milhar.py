'''
Faça um for e imprima na tela todos os numeros de 1 até 1000. Depois, crie uma estrutura condicional para descobrir e printar apenas os números que forem par.  
'''

for i in range (1, 1001):
    mensagem = f'O número {i} é par!'
    if i%2 == 0:
        print(mensagem)