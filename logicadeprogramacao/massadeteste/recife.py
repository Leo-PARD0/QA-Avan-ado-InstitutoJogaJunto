import pandas as pd
 
# Criar os dados em formato de dicionário
dados = {
    "Nome": ["Dione", "Ágatha", "Kaio", "Isabela", "Caique", "Rafael", "Camila"],
    "Idade": [30, 25, 27, 35, 29, 32, 40],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}
# Criar o DataFrame
df = pd.DataFrame(dados)
 
# Exibir o DataFrame completo
print("DataFrame completo:\n")
print(df)
 
# Filtrar apenas os moradores de Recife
recife_df = df[df["Cidade"] == "Recife"]
print("\n Moradores de Recife:\n")
print(recife_df)