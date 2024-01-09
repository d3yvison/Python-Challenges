##Ler um número e devolver dobro, triplo e raíz quadrada
n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro desse número é igual a {} \n O triplo é igual a {} \n E sua raíz quadrada é {:.2f}' .format(d , t , r)) 