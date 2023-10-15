def somar(*valores, b):
    print(valores)
    for valor in valores:
        b *= valor
    print('O valor é :',b)

somar(10,20,5, b=5)