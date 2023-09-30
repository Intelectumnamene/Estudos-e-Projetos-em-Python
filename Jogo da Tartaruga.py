from turtle import Turtle

t = Turtle()
t.speed(1)
while True :
    distancia = int(input('Qual distancia você quer percorre?'))
    t.forward(distancia)
    direita = int(input('Quantos passos para a direita você deseja?'))
    t.right(direita)
    distancia2 = int(input('Qual distancia você deseja percorrer?'))
    t.forward(distancia2)
    esquerda = int(input('Quantos passos para a esquerda você deseja?'))
    t.left(esquerda)
    distancia3 = int(input('Qual distancia você deseja pecorrer?'))
    t.forward(distancia3)
    para_trás = int(input('Quantos passos para trás?'))
    t.backward(para_trás)
    resposta = input('Continuar andando?')
    if resposta not in ('Sim' , 's'):
        break

    input()
