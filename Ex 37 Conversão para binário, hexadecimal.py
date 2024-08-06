# Ler um número inteiro e pedir ao usuário para escolher a base de conversão entre as três opções seguintes
# 1 binário ; 2 octal ; 3 hexadecimal
print('\33[1;36m-=' * 25)
print('\33[1;36m CONVERSÃO PARA BINÁRIO, OCTAL OU HEXADECIMAL')
print('\33[1;36m-=' * 25)

n = int(input('Digite um número inteiro: '))
print('\33[1;36m [1] para base de conversão para Binário')
print('\33[1;36m [2] para base de conversão Octal') 
print('\33[1;36m [3] para Hexadecimal: ')

opcao = int(input('Sua opção de conversão: '))
if opcao == 1 :
    print('{} convertido para Binário é igual a {}' .format(n, bin(n)[2:]))
elif opcao == 2 :
    print('{} convertido para Octal é igual a {}' .format(n, oct(n)[2:]))
elif opcao == 3 :
    print('{} para Hexadecimal é igual a {}' .format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
