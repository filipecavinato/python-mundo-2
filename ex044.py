# Script criado por Filipe Cavinato

p = float(input('Digite o valor do produto: '))
print('Escolha sua forma de pagamento:')
print('[1] - À Vista (Dinheiro/Cheque)')
print('[2] - À Vista no Cartão')
print('[3] - Até 2x no Cartão')
print('[4] - 3x ou mais no Cartão')
op = int(input('Opção: '))

if op == 1:
    print('Você ganhou 10% de desconto!')
    print(f'Preço a pagar: R$ {p - p*0.1}')
elif op == 2:
    print('Você ganhou 5% de desconto!')
    print(f'Preço a pagar: R$ {p - p * 0.05}')
elif op == 3:
    print(f'Preço a pagar: R$ {p}')
elif op == 4:
    print('Juros do Parcelamento de 20%')
    print(f'Preço a pagar: R$ {p + p * 0.2}')
else:
    print('Opção Invalida! Tente novamente..')
