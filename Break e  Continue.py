
#continue, ignora/pular
# for numero in range(100):
#     if numero %2 == 0:
#         print(numero)
#     else:
#          continue

#break, para interromper a iteração.

# for numero in range(100):
#     if numero %2 ==0:
#         print(numero)
#     else:
#          break


frutas = ['Maça', 'Manga', 'Laranja','Morango']
for fruta in frutas:
    if fruta == 'Manga':
        break
    print('Adicionada a dieta {}'.format(fruta))
