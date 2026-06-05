# Script criado por Filipe Cavinato

r1 = float(input('Digite o tamanho do 1º lado: '))
r2 = float(input('Digite o tamanho do 2º lado: '))
r3 = float(input('Digite o tamanho do 3º lado: '))

if r3 < (r1 + r2) and r2 < (r1 + r3) and r1 < (r2 + r3):
    if r1 == r2 == r3:
        print(f'Os lados [{r1, r2, r3}] formam um triangulo Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print(f'Os lados [{r1, r2, r3}] formam um triangulo Isósceles')
    else:
        print(f'Os lados [{r1, r2, r3}] formam um triangulo Escaleno')
else:
    print(f'Os lados [{r1, r2, r3}] não formam um triangulo')
