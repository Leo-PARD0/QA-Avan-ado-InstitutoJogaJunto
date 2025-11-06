aluno = []

nome = input("Digite seu nome: ")

aluno.append(nome)

sim = str(input("Deseja calcular sua média de notas? (S/N): "))

while not sim.lower() == "s" and not sim.lower() == "n":
    sim = input("Resposta inválida. Deseja calcular sua média de notas? (S/N): ")

notas = []

while sim.lower() == "s":
    notas.append(float(input("Digite uma nota: ")))
    sim = str(input("Deseja adicionar mais uma nota? (S/N): "))
    if not sim.lower() == "s" or sim.lower() == "n":
        while not sim.lower() == "s" and not sim.lower() == "n":
            sim = input("Resposta inválida. Deseja adicionar mais uma nota? (S/N): ")

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

aluno.append(media)
aluno.append(notas)

print(f"Aluno: {aluno}")