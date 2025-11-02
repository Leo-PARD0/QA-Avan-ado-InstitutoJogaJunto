'''
EM SQUAD

Leiam o case e resolvam a situação.

A Loja do Joga Junto conta mais uma vez com a colaboração do seu squad! Desta vez, surge a necessidade de desenvolver um programa que analisa o CEP inserido pelo usuário e determina se ele é elegível para frete grátis. Para realizar essa tarefa, foi definida uma política de frete grátis abrangendo todos os estados das regiões Norte e Nordeste do país.  


Faça um brainstorming com sua equipe sobre o fluxo e requisitos necessários para construção desse programa
--> lista de cep com desconto
----> api para request cep?
-------> request para receber uf do estado
-------> lista com ufs do norte e nordeste
----> Norte e nordeste
--> receber cep usuario
--> comparar cep usuario com lista cep
----> se cep usuario in lista cep imprime frete gratis


Desenvolva o programa


Faça casos de teste para este cenário, documente os testes realizados e insira no Bitrix


Caso seja encontrado algum bug no seu código, documente-o. a
'''

def extrair_dados(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/" # api do viacep para buscar os dados do cep
    resposta = requests.get(url) # variável para verificar a comunicação do via cep

    if resposta.status_code == 200:
        dados = resposta.json() # transforma dados em um dicionário com todos os dados do cep
    else:
        print('Algo de errado com viaCEP.')
    return dados # retorna o dicionario dados

def verificar_desconto(dados):
    uf = dados.get('uf', 'cep não encontrado') # recebe
    if uf in estados:
        print(uf)
        print(tem_desconto)
    else:
        print(uf)
        print('Siga com a compra')

import requests

estados = ['AC', 'AP','AM','PA','RO','RR','TO','AL','BA','CE','MA','PB','PE','PI','RN','SE']
# NORTE: Acre (AC), Amapá (AP), Amazonas (AM), Pará (PA), Rondônia (RO), Roraima (RR) e Tocantins (TO)
# NORDESTE: Alagoas (AL), Bahia (BA), Ceará (CE), Maranhão (MA), Paraíba (PB), Pernambuco (PE), Piauí (PI), Rio Grande do Norte (RN) e Sergipe (SE)

tem_desconto = 'FRETE GRATIS'

cep = int(input('Digite seu cep [APENAS NÚMEROS]: ')) # recebe cep de usuário

dados = extrair_dados(cep)

verificar_desconto(dados)
