# Ler 3 números e mostrar qual é o maior e qual o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# Validação do menor
if n1 < n2 and n1 < n3 :
    menor = n1
if n2 < n1 and n2 < n3 :
    menor = n2
if n3 < n2 and n3< n1 :
    menor = n3
#Validação do maior
if n1 > n2 and n1 >n3 :
    maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n2 and n3 > n1 :
    maior = n3
print('O maior número é {} e o menor é {}'.format(maior , menor))
