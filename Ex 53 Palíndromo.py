#Ler uma frase e dizer se é um palíndromo desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra] #inverso += forma pythonica
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')