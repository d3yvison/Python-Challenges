# Ler dois números inteiros e compará-los exibindo os seguintes resultados:
# O primeiro valor é maior , O segundo valor é maior ou Não existe maior, os dois são iguais
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2 :
    print('O número {} é o maior número, e o {} é o menor. '.format(n1 , n2))
elif n2 > n1 :
    print('O número {} é o maior, e o número {} é o menor. '.format(n2 , n1))
else:
    print('Os números são iguais!')
