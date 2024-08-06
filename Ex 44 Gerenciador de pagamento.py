# Calcular um valor a ser pago por um produto considerando seu preço normal e as condições de pagamento:
# À vista dinheiro/cheque 10% de desconto ; À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal ; 3x ou mais no cartão 20% de juros
preco = float(input('Informe o valor do produto: R$ '))
print('Digite 1 para pagamento à vista (dinheiro/cheque 10% de desconto) ')
print('Digite 2 para pagamento à vista no cartão (5% de desconto) ')
print('Digite 3 para até 2x no cartão ')
print('Digite 4 para 3x ou mais no cartão (acréscimo de 20% de juros) ')
# Feito em prints separados para facilitar visualização e didática, mas em situação profissional seria utilizado 
# quebra de linha ao invés de recrutar a função 'print' múltiplas vezes.
pgto = int(input('Digite a opção de pagamento escolhida (1, 2 , 3 ou 4): '))
if pgto == 1 :    
    preco = preco - (preco * 0.10)
    print('Opção 1 selecionada - Pagamento à vista(dinheiro/cheque). O valor do produto será: R${:.2f} '.format(preco))
elif pgto == 2 :
    preco = preco - (preco * 0.05)
    print('Opção 2 selecionada - Pagamento à vista no cartão. O valor do produto será: R${:.2f}'.format(preco))
elif pgto == 3 :
    preco = preco / 2
    print('Opção 3 selecionada - Pagamento em 2x de R${:.2f}' .format(preco))
elif pgto == 4 :
    preco = preco + (preco * 0.20)
    print('Opção 4 selecionada - Pagamento em 3x ou mais selecionada. O valor total do produto será: R${:.2f}' .format(preco))
else:
    print('Opção inválida selecionada!')