# Validar se dado três retas é possível formar um triângulo
# Acrescentar qual tipo de triângulo será formado:
# Equilátero: Todos os lados iguais ; Isósceles: Dois lados iguais ; Escaleno: Todos os lados diferentes 
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    print('Condição de existência de triângulo verdadeira!')
    if r1 != r2 != r3 != r1 :
        print('Será formado um triângulo Escaleno')
    elif r1 == r2 or r1 == r3 or r2 == r3 :
        print('Será formado um triângulo Isósceles')
    elif r1 == r2 == r3 :
        print('Será formado um triângulo Equilátero') 
    # Poderia utilizar um 'else' na última opção mas queria guardar todas as formas completas para
    # futura consulta.

else:
    print('Condição de existência de triângulo falsa!')
