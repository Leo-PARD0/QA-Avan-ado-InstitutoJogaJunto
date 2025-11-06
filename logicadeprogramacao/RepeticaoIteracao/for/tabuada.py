'''
Crie a estrutura de uma tabuada para um valor inserido. O resultado deverá ser printado do valor multiplicado de 1 a 10. 
'''

for n in range(1,11):
    for i in range(1,11):
        valor = n*i
        print(f'{n} X {i} = {valor}')

n = int(input('Digite um valor para saber sua tabuada: '))
for i in range(1,11):
    valor = n*i
    print(f'{n} X {i} = {valor}')