#Ler o peso de 5 pessoas e informar o maior e menor peso informados.
maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é: {}Kg'.format(maior))
print('E o menor peso é: {}Kg'.format(menor))