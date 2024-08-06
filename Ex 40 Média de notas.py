# ler duas notas de um aluno e calcular a média devolvendo a mensagem de acordo com os parâmetros:
# abaixo de 5.0 reprovado ; 5.0 a 6.9 recuperação ; 7.0 ou superior aprovado.
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
resultado = (n1 + n2) / 2
if resultado < 5 :
    print('Sua média foi: {:.1f} Infelizmente você foi reprovado!' .format(resultado))
elif resultado == 5 and resultado <=  6.9 :
    print('Sua média foi: {:.1f} Você está em  recuperação!' .format(resultado))
else:
    print('Sua média foi: {:.1f} Parabéns, você foi aprovado!' .format(resultado))
