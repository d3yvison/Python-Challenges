#Soma de todos os números ímpares divisíveis por 3 entre 1 e 500
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n                #soma += n (forma pythonica)
        contador = contador + 1        #contador += 1 (forma pythonica)
print('A soma de todos os {} valores é {}'.format(contador, soma))
    