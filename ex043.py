# Script criado por Filipe Cavinato

peso = float(input('Digite o seu peso (em Kg): '))
altura = float(input('Digite a sua altura (em m): '))
imc = peso/pow(altura,2)

print(f'IMC = {imc:.2f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
