# Ler o ano de nascimento e informar se ele terá que se alistar ao exército brasileiro
from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade < 18 :
    diferenca = 18 - idade
    print('Ainda não chegou sua hora de se alistar, falta(m) {} ano(s).' .format(diferenca))
elif idade == 18:
    print('Chegou a hora de fazer o seu alistamento.')
else:
    diferenca = idade - 18
    print('Você deveria ter se alistado há {} ano(s).' .format(diferenca))


