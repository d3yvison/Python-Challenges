#Programa que mostra todos os números pares até 50

for n in range(0,51):
    if n % 2 == 0:
        print(n, end=' ') #Para imprimir todos na mesma linha com espaço entre os números    
#Otimizando o códio acima usando metade dos Steps:
# for n in range (2, 51, 2):
#Não sendo necessário o If evitando passar por todas as iterações.