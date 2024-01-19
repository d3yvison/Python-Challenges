# Ler o valor de um imóvel, o salário e em quantos anos será pago
# A parcela mensal não pode exceder 30% do salário
print('\33[1;31m=' * 45 )
print('\33[1;31m AVALIAÇÃO DE FINANCIAMENTO IMOBILIÁRIO ')
print('\33[1;31m=' * 45)
preco = float(input('Qual é o valor do imóvel: R$'))
salario = float(input('Qual é o valor do seu salário: R$'))
prazo = float(input('Em quantas parcelas deseja pagar: '))
parcela = preco / prazo
if parcela <= salario * 0.3 :
    print('\33[1;32m Parabéns, o seu financiamento foi aprovado!!!')
else:
    print('\33[1;31m Infelizmente o seu financiamento não foi aprovado!')
