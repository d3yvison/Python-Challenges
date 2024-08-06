#Ler um número inteiro e descobrir se é um número primo ou não
n = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
    else:
        print('{}'.format(c), end=' ')
print('O número {} foi divisível {} vezes' .format(n, total))
if total == 2:
    print('Portanto ele é um número primo!')
else:
    print('Portanto ele não é um número primo!')
