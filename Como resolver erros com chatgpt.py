#erro genérico
#1-Leia o erro no terminal geralmente esta com a palavra indexerro.
#2-copie a mensagem e coloque no google tradutor.
#3-tente entender o que fazer a partir da menasagem.
nome = 'amanda'
#indice'012345'
print(nome[3])

#erro específico (Inclue dados da sua aplicão. Possivelmente estará na linha de comando.)

with open ('senhas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
