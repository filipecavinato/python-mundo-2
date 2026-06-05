# Script criado por Filipe Cavinato

print('Fibonacci')
n = int(input('Digite a quantidade de termos que quer ver: '))
fib = fib_2ant = 0
fib_1ant = 1
c = 1
while c <= n:
    if c == 1:
        print(fib_2ant, end=' ')
    elif c == 2:
        print(fib_1ant, end=' ')
    else:
        fib = fib_1ant + fib_2ant
        fib_2ant = fib_1ant
        fib_1ant = fib
        print(fib, end=' ')
    c += 1
print('\n------ Fim do Programa ------')
