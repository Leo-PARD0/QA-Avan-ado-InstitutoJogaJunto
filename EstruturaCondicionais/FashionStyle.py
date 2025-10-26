compra = float(input("Qual o valor da sua compra em reais? "))
desconto = 0
desconto_ideal = 0
mensagem = " "

if (compra < 250):
    desconto_ideal = 10
    mensagem = f"Poxa, faltou R$ {250-compra:.2f} para você obter {desconto_ideal}% de desconto."
    print(mensagem)
elif (compra >= 250 and compra < 500):
    desconto = 10
    desconto_ideal = 30
    mensagem = f"Você conseguiu {desconto}% de desconto! faltam R$ {500-compra:.2f} para você ganhar {desconto_ideal}% de desconto."
    print(mensagem)
else :
    desconto = 30
    mensagem = f"PARABÉNS, VOCÊ RECEBEU UM DESCONTÃO DE {desconto}%"
    print(mensagem)


'''
compra >= 250 desconto and < 500 = 10 mensagem = voce conseguiu 10%, faltam 500-compra para você ganhar 30%
compra <250 desconto = 0 mensagem = Poxa, faltou 250-compra para você obter desconto
compra  >= 500 desconto = 30 mensagem = Uau, você recebeu um descontão de 30%
'''
