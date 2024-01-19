# Calcular o valor de aumetno em um salário informado.
# Para salários superiores a R$1.250,00 calcular aumento de 10%
# Para inferiores ou iguais o aumento é de 15%
salario = float(input('Digite o salário: R$'))
if salario > 1250 :
    aumento = salario + (salario * 0.10)
    print('O novo salário será: R${:.2f}' .format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('O novo salário será: R${:.2f}' .format(aumento))