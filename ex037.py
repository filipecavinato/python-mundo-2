# Script criado por Filipe Cavinato

v = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão: ')
print('[1] - Binario')
print('[2] - Octal')
print('[3] - Hexadecimal')
op = int(input('Opção: '))

if op == 1:
    print(f'O número {v} em Binario é {bin(v)[2:]}')
elif op == 2:
    print(f'O número {v} em Octal é {oct(v)[2:]}')
elif op == 3:
    print(f'O número {v} em Hexadecimal é {hex(v)[2:]}')
else:
    print('Opção invalida! Tente novamente...')
