#Ler um número de 4 dígitos e devolver unidade, dezena, centena e milhar do mesmo
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
print('Unidade: {}'.format(u))
d = n // 10 % 10
print('Dezena: {}' .format(d))
c = n // 100 % 10
print('Centena: {}' .format(c))
m = n // 1000 % 10
print('Milhar: {}' .format(m))