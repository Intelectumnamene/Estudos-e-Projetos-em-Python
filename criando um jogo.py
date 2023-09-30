from turtle import Turtle
#Inicializar uma turtle
t = Turtle()
#Definir velocidade
t.speed(1)
while True :
    distancia = int(input("Qual distâcia devo percorre? "))
    t.forward(distancia)

#Movimentar a turtle para frente
#rotacionar em X graus para a direita
t.right(90)
t.forward(100)
#rotacionar em X graus para a direita
t.left(90)
t.forward(100)
#Movimentar a turtle para trás
t.backward(200)
input()