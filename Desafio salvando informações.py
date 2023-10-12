import os
frutas = ['Banana', 'Maça', 'Abacate', 'Limão', 'Jabuticaba']
cores = ['Azul', 'Verde', 'Amarelo', 'Preto', 'Branco']
top_5_liguagens =['Python','Java','JavaScript','C++','Ruby']


with open('frutas.txt','w',encoding= 'utf-8',newline='') as arquivo:
    for fruta in frutas:
       arquivo.write(fruta + os.linesep)

#imprima na tela todas as linhas que estão dentro do arquivo frutas.txt
with open('frutas.txt','r', encoding='utf-8')as arquivo:
   for linha in arquivo:
      print(linha)

#sem apagar os dados que já estão dentro dos arquivos de frutas.txt, adicione todas as cores que estão
#dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt','a',encoding='utf-8', newline='')as arquivo:
   for cor in cores:
      arquivo.write(os.linesep + cor )

# with open('frutas.txt', 'r', encoding='utf-8', newline= '') as arquivo:
#     for fruta, cor in zip(frutas, cores):
#         arquivo.write(fruta + '-' + cor + os.linesep)
with open('Top 5 linguagens', 'w', encoding='utf-8',newline='') as arquivo:
      for linguagem in top_5_liguagens:
       arquivo.write(linguagem + os.linesep)

#Criando vários arquivos vazios usando um laço for.

arquivos = ['musica.mp3','foto.jpg','senhas.txt','relatorio.pdf',]
for arquivo in arquivos:
   with open(arquivo,'w')as arquivo:
      pass