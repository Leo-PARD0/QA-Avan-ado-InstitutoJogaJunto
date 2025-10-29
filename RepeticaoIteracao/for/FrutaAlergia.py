frutas = ["maçã", "banana", "laranja", "morango", "uva"] # lista de frutas no banco de dados
alergias = [] # lista de alergias vazia

alergias.append(input("Digite uma fruta que você é alérgico(a): ").lower()) # usuario adiciona fruta alergica

for fruta in frutas: # para cada 'fruta' em 'frutas'
    if fruta in alergias: # se 'fruta' em 'alergias'
        print(f"Atenção! Você é alérgico(a) a {fruta}. Evite consumi-la.")
    else:
        pass