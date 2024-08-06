# Jogo Jokenpo (Pedra-Papel-Tesoura)
import random
import time

print('\33[1;36m=-' * 25)
print('\33[1;36m JO KEN PÔ')
print('\33[1;36m PEDRA - PAPEL - TESOURA')
print('\33[1;36m=-' * 25)

jogador = int(input('Digite 0 para Pedra, 1 para Papel e 2 para Tesoura: '))
computador = random.randint(0, 2)

print('\33[1;40mCarregando Resultados...')
time.sleep(1.5)

if jogador == 0 and computador == 0 :
    print('\33[1;43mEmpate!')
elif jogador == 0 and jogador == 1 :
    print('\33[1;41mVocê perdeu!')
elif jogador == 0 and computador == 2 :
    print('\33[1;42mParabéns, Você Ganhou!!!')

elif jogador == 1 and computador == 0 :
    print('\33[1;42mParabéns, Você Ganhou!!!')
elif jogador == 1 and computador == 1 :
    print('[1;43mEmpate!')
elif jogador == 1 and computador == 2 :
    print('\33[1;41mVocê Perdeu!')

elif jogador == 2 and computador == 0 :
    print('\33[1;41mVocê Perdeu!')
elif jogador == 2 and computador == 1 :
    print('\33[1;42mParabéns, Você Ganhou!!!')
elif jogador == 2 and computador == 2 :
    print('[1;43mEmpate!')
else: 
    print('\33[1;41mOpção inválida!')