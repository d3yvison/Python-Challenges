##Sorteio quatro nomes exibindo qual posição de cada um
from random import shuffle
n1 = str(input('Insira o nome do primeiro participante: '))
n2 = str(input('Insira o nome do segundo participante: '))
n3 = str(input('Insira o nome do terceiro participante: '))
n4 = str(input('Insira o nome do quarto participante:'))
nomes = [n1 , n2 , n3 , n4]
shuffle(nomes)
print('A ordem dos vencedores é: {}' .format(nomes))