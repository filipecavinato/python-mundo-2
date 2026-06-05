# Script criado por Filipe Cavinato

soma = 0
qt = 0
lista_h = ['', 0, '']
for i in range(1,5):
    print(f'{i}ª Pessoa: ')
    nome = str(input('Digite o nome: ')).strip().capitalize()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()

    soma += idade
    if idade > lista_h[1]:
        lista_h = [nome, idade, sexo]
    if sexo == 'F' and idade < 20:
        qt += 1

media = soma/4
print(f'A média de idade do grupo é {media} anos')
print(f'O Homem mais velho é o {lista_h[0]} com {lista_h[1]} anos')
print(f'Há {qt} mulheres com menos de 20 anos')
