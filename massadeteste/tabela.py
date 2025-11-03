import pandas as pd

pessoas = {
    'nome' : ['João', 'Marta', 'Ary', 'Matheus', 'Michele'],
    'idade': [51,37,23,24,33]
}

df = pd.DataFrame(pessoas)

print(df)