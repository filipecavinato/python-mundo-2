# Script criado por Filipe Cavinato

frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
palindromo = str('').upper()

for letra in reversed(frase):
    palindromo += letra

print(f'Frase Original: {frase}')
print(f'Frase Invertida: {palindromo}')

if palindromo == frase:
    print('A Frase é um Palíndromo!')
else:
    print('A frase não é um Palíndromo!')
