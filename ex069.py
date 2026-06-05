# Script criado por Filipe Cavinato

qt = [0, 0, 0, 0]
# qt[qt total, +18, homens, mulheres]
while True:
    print('-----------------')
    print(f'Cadastro Pessoa {qt[0] + 1}')
    print('-----------------')
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Qual o sexo ? [M/F] ')).strip().upper()
        if sexo in 'MF':
            break
    if idade >= 18:
        qt[1] += 1
    if sexo == 'M':
        qt[2] += 1
    if sexo == 'F' and idade < 20:
        qt[3] += 1

    qt[0] += 1
    while True:
        op = str(input('Quer cadastrar mais pessoas ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
print('---------------------')
print(f'Total de cadastros: {qt[0]}')
print(f'{qt[1]} pessoas tem mais de 18 anos\n{qt[2]} Homens foram cadastrados\n{qt[3]} mulheres com menos de 20 anos\n')

print('------ Fim do Programa ------')
