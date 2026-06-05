# Script criado por Filipe Cavinato

lista = ['M', 'F']
sexo = ''

while sexo not in lista:
    sexo = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0]
    if sexo not in lista:
        print('Formato Invalido! Informe apenas M ou F')
    else:
        print(f'Sexo Digitado: {sexo}\nStatus: Registrado com Sucesso\n')

print('------ Fim do Programa ------')
