## Ler o valor antigo e atribuir o desconto de 5% 
preco = float(input('Digite o preço total sem desconto: R$'))
desconto = preco * 0.05
print('O valor do produto com 5% de desconto será: R${:.2f}' .format(preco - desconto))
