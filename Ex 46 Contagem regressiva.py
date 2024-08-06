#Contagem regressiva começando de 10 e com intervalos de 1 segundo
import time
#"from time import sleep" é mais eficiente para importar somente o necessário

for n in range(10,-1,-1):
    print(n)
    time.sleep(1)
print('FELIZ ANO NOVO!!!')
