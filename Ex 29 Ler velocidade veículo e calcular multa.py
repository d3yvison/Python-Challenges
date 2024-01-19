# Ler a velocidade de um veículo e se ultrapassar 80KM/h mostre uma mensagem notificando;
# A multa vai custar $7,00 por KM acima do limite
velocidade = int(input('Velocidade registrada: '))
if velocidade >80 :
    multa = (velocidade - 80) * 7
    print('Multa de R${:.2f} aplicada devido à excesso de velocidade! '.format(multa))
else:
    print('Velocidade dentro do limite da via.')    