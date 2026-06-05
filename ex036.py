# Script criado por Filipe Cavinato

val_casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salario: R$ '))
t = int(input('Em quantos anos você vai pagar: '))
val_parc = val_casa/(t*12)

print(f'Casa de R$ {val_casa:.2f} para pagamento em {t} anos')
print(f'Prestação Mensal de R$ {val_parc:.2f}')
if val_parc <= sal*0.3:
    print('Empréstimo Aprovado!')
else:
    print('Seu empréstimo foi negado!\nEle compromete mais de 30% do seu salario')
