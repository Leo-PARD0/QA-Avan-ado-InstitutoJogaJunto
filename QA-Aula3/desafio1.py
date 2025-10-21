print ("Olá, tudo bem?")
print ("Estou realizando um cadastro,")
nome = input ("Poderia me dizer seu nome? ")
print (f"Muito prazer, {nome}!")
idade = int(input (f"Quantos anos você tem, {nome}? "))

if idade >= 18:
    print (f"Então você já é maior de idade, {nome}")
else:
    print (f"Po, aconselho que você não continue com o código pois estará passando dados sensíveis...")

print ("Vamos continuar...")

altura = str(input (f"Qual a sua altura em metros, {nome}? "))
altura_num = float(altura.replace(",","."))

if idade < 18:
    print (f"Legal que você completou o registro, {nome}, mas eu vou excluir seus dados por segurança. Nem todos os robos são tão legais quanto eu. Existem robos realmente ruins por aí...")
    print (f"TOMA CUIDADO COM SEUS DADOS NA INTERNET! {nome} de {idade} anos.")
else:
    print ("Cadastro concluido com sucesso! Aqui estão os seus dados: ")
    print (f"Nome: {nome}")
    print (f"Idade: {idade} anos")
    print (f"Altura: {altura} metros")

print ("Vamos ver suas notas agora!")

nota1 = str(input("Digite a sua primeira nota: "))
nota1_num = float(nota1.replace(",","."))
nota2 = str(input("Digite a sua segunda nota: "))
nota2_num = float(nota2.replace(",","."))

soma_num = nota1_num + nota2_num
soma = str(f"{soma_num:.2f}")
media_num = (nota1_num + nota2_num)/2
media = str(f"{media_num: .2f}")

print (f"A soma das suas notas é: {soma.replace('.',',')}")
print (f"Sua média é: {media.replace(".",",")}")
