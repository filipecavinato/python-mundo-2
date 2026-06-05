# Script criado por Filipe Cavinato

n = int(input('Você quer ver a tabuada de qual número: '))

print('-=-' * 5)
print(f' Tabuada do {n}')
print('-=-' * 5)

for i in range(1,11):
    print(f'{n} x {i:2} = {n * i}')
