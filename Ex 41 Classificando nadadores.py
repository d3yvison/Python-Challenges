# Dado a idade de um nadador classificar conforme a seguir:
# Até 9 anos Mirim ; Até 14 anos Infantil ; Até 19 anos Junior ; Até 25 anos Sênior ; Acima Master
idade = int(input('Informe sua idade: '))
if idade <= 9 :
    print('Sua categoria é: Mirim')
elif idade <= 14 :
    print('Sua categoria é Infantil')
elif idade <= 19 :
    print('Sua categoria é: Júnior')
elif idade <= 25 :
    print('Sua categoria é: Sênior')
else:
    print('Sua categoria é: Master')