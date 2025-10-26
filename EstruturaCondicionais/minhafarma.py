valor_ideal = 100.00 # caso a promoção mude, mudar este valor.
valor = float(input('Digite o valor total da compra: R$ ').replace(',', '.'))
vale = 10.00 # caso a promoção mude, mudar este valor.

if valor >= valor_ideal:
    vale_str = f"{vale:.2f}".replace('.', ',')
    mensagem = f"SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R${vale_str} REAIS DE DESCONTO."
    print(mensagem)
else:
    valor_ideal_str = f"{valor_ideal:.2f}".replace('.', ',')
    vale_str = f"{vale:.2f}".replace('.', ',')
    mensagem = f"OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R${valor_ideal_str} REAIS GERAM UM VOUCHER DE R${vale_str} REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?"
    print(mensagem)