#Ler ano de nascimento de 7 pessoas e informar quais já são maiores de idade
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for pessoas in range(1,8):
    nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - nascimento
    if idade >= 18:
        maiores = maiores + 1 #pythonic maiores += 1
    else:
        menores = menores + 1 #pythonic menores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
