#Tabuada utilizando laço de repetição
n = (int(input("Digite um número inteiro para saber sua tabuada:")))
for c in range(1,11,):
    print('{} x {:2} = {}' .format(n, c, n*c))