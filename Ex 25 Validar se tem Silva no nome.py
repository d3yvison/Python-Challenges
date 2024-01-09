# Ler um nome e validar se há "Silva" no mesmo (Sem uso de condições)
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem "Silva"? {}' .format('SILVA' in nome.upper()))

