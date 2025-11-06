palavra = str(input("Digite uma palavra: ")).lower()
letras = list(palavra)
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0
for letra in letras:
    if letra in vogais:
        contador += 1
        print (f'{letra}')

print(f'A palavra {palavra} tem {contador} vogais.')
