'''
Agora, criem um scritp para:

Ter um input de usuário para inserir os números de matrícula em uma lista. 

Ter um validador nessa lista que permita a inserção de dados até ocupar 5 espaços index.

Fazer um laço de repetição para passar todos os números da lista em uma função para verificar se o número é par ou ímpar. 
'''

cadastro = {
    'nomes' : [], # a lista de nomes não foi pedida no exercício, mas evita retrabalho no futuro, visto que desta forma o código já vai salvar o nome da pessoa e o número da matricula vinculados ao mesmo index da lista.
    'matriculas' : []
}

def adicionar_aluno():
    nome = input('Digite o seu nome: ')
    matricula = int(input('Digite o número da sua matricula: '))
    cadastro['nomes'].append(nome)
    cadastro['matriculas'].append(matricula)
    return cadastro

while len(cadastro['matriculas']) < 5:
    adicionar_aluno()
    # DEBUG: print(len(cadastro['matriculas']))

par = []
impar = []

for matricula in cadastro['matriculas']:
    if matricula % 2 == 0:
        par.append(matricula)
    else:
        impar.append(matricula)

mensagem = 'As matriculas são:'
pares = f'PARES: {par}'
impares = f'IMPARES: {impar}'

print(f'{mensagem}\n{pares}\n{impares}')