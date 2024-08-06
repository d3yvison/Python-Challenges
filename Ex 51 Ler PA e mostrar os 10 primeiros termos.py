#Ler uma progressão aritmética e no final mostrar os 10 primeiros termos dessa progressão.
print('PROGRESSÃO ARITMÉTICA')
termo = int(input("Digite o valor do primeiro Termo:"))
razao = int(input("Agora informe o valor da Razão:"))
decimo = termo + (11 - 1) * razao
for i in range(termo,decimo,razao):
    print('{}'.format(i), end=' - ')
print('Fim')