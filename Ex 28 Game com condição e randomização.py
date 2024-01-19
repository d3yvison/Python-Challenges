# Computador escolhe um número de 0 a 5 e usuário tem que adivinhar
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
num = random.randint(0, 5)
tentativa = int(input('Digite o número entre 0 e 5 que você acha que o computador escolheu: '))
if num == tentativa:
    print('Parabéns você acertou! ')
else:
    print('Você errou! O número escolhido foi {}'.format(num))