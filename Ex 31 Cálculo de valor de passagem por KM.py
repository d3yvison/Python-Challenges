# De acordo com a distância informada calcular o preço da passagem.
# Será cobrado R$0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distância em KM até o destino? '))
if distancia <= 200 :
    preco = distancia * 0.50
    print('A passagem irá custar R${:.2f}' .format(preco))
else :
    preco = distancia * 0.45
    print('A passagem irá custar R${:.2f}' .format(preco))

