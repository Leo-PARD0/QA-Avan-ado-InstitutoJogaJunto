'''
Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, querem estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos será feita seguindo um critério:

Alunos com número de matrícula par, ficarão no grupo azul.
Alunos com número de matrícula ímpar, ficarão no grupo amarelo. 
Os alunos ainda não sabem dessa regra de separação dos grupos e, no dia do evento, quando digitarem o número da matrícula na catraca, deve aparecer no painel a cor do grupo que ele deve integrar. 

DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

Caso o número de matrícula do(a) aluno(a) seja par imprima:
VOCÊ ESTÁ NO TIME AZUL

Caso o número de matrícula do(a) aluno(a) seja impar imprima:
VOCÊ ESTÁ NO TIME AMARELO
'''

def amarelo_azul (matricula):
    if matricula % 2 == 0:
        numero = "PAR"
    else:
        numero = "IMPAR"
    return numero

matricula = int(input('Digite o número da sua matrícula: '))

amarelo_azul(matricula)

if amarelo_azul(matricula) == "PAR":
    print('VOCÊ ESTÁ NO TIME AZUL')
else:
    print('VOCÊ ESTÁ NO TIME AMARELO')

'''
Inicialmente eu fiz desse jeito, li o case denovo e percebi que a função deve retornar se é impar ou par, então eu mudei para o código acima. Porém, o meu código inicial cumpre a função de maneira mais otimizada, pois a função já verifica a paridade na condicional, o resultado da paridade é o time que o aluno irá integrar. Não há necessidade de repetir uma condicional para verificar se a função retornou par ou impar.

def amarelo_azul (matricula):
    if matricula % 2 == 0:
        mensagem = "VOCÊ ESTÁ NO TIME AZUL"
    else:
        mensagem = "VOCÊ ESTÁ NO TIME AMARELO"
    return mensagem

matricula = int(input('Digite o número da sua matrícula: '))

print(amarelo_azul(matricula))
'''