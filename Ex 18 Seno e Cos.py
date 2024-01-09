## Ler um ângulo e calcular o seno e cosseno e tangente
import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Os resultados são - Seno: {:.2f} , Cosseno: {:.2f} e Tangente: {:.2f}' .format(sen,cos,tan))