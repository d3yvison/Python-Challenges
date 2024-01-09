#Ler algo e devolver o tipo primitivo entre outros.
n = input('Digite algo:')
print('O tipo primitivo desse valor é:' , type(n))   
print('É um número?' , n.isnumeric())
print('Está completamente em letras maiúsculas?' , n.isupper())
print('Está completamente em letras minúsculas?' , n.islower())
print('Está capitalizada?' , n.istitle())

