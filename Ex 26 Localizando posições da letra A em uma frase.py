# Ler uma frase e mostrar quanstas letras A temos, qual a posição da primeira e da última
frase = str(input('Digite uma frase: ')).upper().strip
print('A letra A aparece {} vezes' .format(frase.count('A')))
print('A primeira letra A aparece na posição {}' .format(frase.find('A')+1))
print('A última letra A aparece na posição {}' .format(frase.rfind('A')+1))
# '+1' utilizado para mostrar a posição acrescido de 1 visto que a contagem se inicia no zero. 
