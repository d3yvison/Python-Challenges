# Calcular IMC e devolver os resultados de acordo com as informações a seguir:
# Abaixo de 18.5: Abaixo do peso ; Entre 18.5 e 25: Peso ideal ;
# 25 até 30: Sobrepeso ; 30 até 40: Obesidade ; Acima de 40: Obesidade mórbida
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura * altura)
if imc < 18.5 :
    print('Você está abaixo do peso.')
elif imc > 18.4 and imc < 25.1 :
    print('Você está no peso ideal.')
elif imc > 24.9 and imc < 30.1 :
    print('Você está em sobrepeso.')
elif imc > 30 and imc < 40.1 :
    print('Você está em obesidade.')
else: 
    print('Você está num quadro de obesidade mórbida.')

