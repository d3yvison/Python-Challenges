## Soteio entre quatro nomes
from random import choice
n1 = str(input('Digite o primeiro nome a sortear: '))
n2 = str(input('Digite o segundo nome de participante: '))
n3 = str(input('Digite o nome do terceiro participante: '))
n4 = str(input('Digite o nome do quarto participante: '))
nomes = [n1 , n2 , n3 , n4] 
sorteado = choice(nomes)
print('{} foi o(a) vencedor(a)!'.format(sorteado))