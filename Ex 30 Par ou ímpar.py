# ler um número inteiro e devolver se é par ou ímpar
num = int(input('Digite um número para saber se é par ou ímpar: '))
if num % 2 == 0:
    print('O número {} é par! '.format(num))
else:
    print('O número {} é ímpar! ' .format(num))
