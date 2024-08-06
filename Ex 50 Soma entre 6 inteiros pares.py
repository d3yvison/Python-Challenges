#Ler 6 números inteiros e mostrar a soma apenas dos pares, os ímpares desconside-os
for c in range(0,6):
    n = int(input("Digite um número inteiro:"))
    if n % 2 == 0:
       result = n+n
print(result)

