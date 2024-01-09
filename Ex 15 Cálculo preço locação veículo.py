## Cálculo total de locação de veículo sabendo que a diária custa R$60, e o KM rodado R$0,15
dias = float(input('Quantos dias o veículo foi alugado?'))
km = float(input('Quantos kilômetros foram percoridos?'))
print('O custo total do aluguel será: R${}' .format(dias * 60 + km * 0.15))