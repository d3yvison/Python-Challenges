## Ler altura e largura da parede e calcular quantos litros de tinta serão necessários
## Sabendo que cada lata corresponde a 2 metros quadrados
a = float(input('Digite a altura da parede:'))
l = float(input('Digite a largura da parede:'))
area = a * l
r = area / 2
print('Serão necessárias {} lata(s) de tinta para pintar essa parede!' .format(r))
