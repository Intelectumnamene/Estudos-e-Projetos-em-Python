nomes = ["Larissa", "Rafael", "Marcos", "john"]


def pessoa_aprovada(pessoa):
    if pessoa == "Marcos":
        return True
    else:
        return False


print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))


pinturas = [
    ["Pintura Classica", "Azul", 1857],
    ["Pintura Medieval", "Vermelha", 1867],
    ["Pintura Moderna", "Verde", 1897],
]


def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False


print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))
