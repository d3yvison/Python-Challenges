# Ler o nome de uma cidade e dizer se começa ou não com a palavra 'Santo'
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[0:5].lower() == 'santo')
