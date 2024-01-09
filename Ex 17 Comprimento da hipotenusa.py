## Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
## Calcule e mostre o comprimento da hipotenusa
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
h = (co ** 2) + (ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}' .format(h))
## Também é possível fazer importando da bibioteca math com o comando ' hypot(x,y) '.