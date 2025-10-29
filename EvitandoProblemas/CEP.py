import requests

integrantes = { }

continuar = True

while continuar == True:
    nome = input("Digite o nome do usuário: ")
    cep = input("Digite o CEP do usuário (somente números): ")
    integrantes[nome] = cep
    resposta = input("Deseja adicionar outro usuário? (s/n): ")
    if resposta.lower() != 's':
        continuar = False

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f'{nome} mora na cidade {cidade}.')
    else:
        print(f'Não foi possível obter os dados para o CEP {cep}.')
