'''
Vamos criar uma função chamada calcular_preco_total que aceita o valor total da compra e a porcentagem de desconto como argumentos e retorna o preço total após aplicar o desconto. Aqui está como poderia ser o código:
'''

def calcular_preco_total(valor_total, percentual_desconto):
    valor_desconto = valor_total * percentual_desconto
    return valor_total - valor_desconto

valor_total = float(input('Digite o valor total da compra: '))
percentual_desconto = int(input('Digite a porcentagem de desconto (sem o %): ')) / 100

preco_final = calcular_preco_total(valor_total, percentual_desconto)
print(f'O preço total após o desconto é: R$ {preco_final:.2f}')