# Ler um nome competo e mostrar o nome com todas as letras maiúsculas e minúsculas;
# Quantas letras ao todo desconsiderando espaços); Total de letras 1° nome
nome = str(input('Digite o seu nome completo: '))
print('Formatado em letras maiúsculas: {}'.format(nome.upper())) 
print('Formatado em letras minúsculas: {}'.format(nome.lower()))
print('O total de letras do seu nome completo é {} letras'.format(len(nome) - nome.count(' ')))
#print('O total de letras do seu primeiro nome é {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem um total de {} letras.'.format(separa[0], len(separa[0])))