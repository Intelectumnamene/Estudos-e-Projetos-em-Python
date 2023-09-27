frase = 'Olá, bem-vindo a este treinamento!'
print(frase)
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
print('====================')
nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))
print('====================')
hashtags = '#music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
print('====================')
#como concatenar (combinar) strings
hastag_separadas_por_espaço = hashtags.split(' ')
print(','.join(hastag_separadas_por_espaço))
print('-'.join(hastag_separadas_por_espaço))
print('.'.join(hastag_separadas_por_espaço))
print('====================')