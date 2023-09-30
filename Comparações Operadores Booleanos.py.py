idade = 21
possui_convite = False
filho_do_dono = True
print(idade >= 21) and (possui_convite == True)
print(idade >= 21 or possui_convite == True)
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

maior_de_idade = 18
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

print(maior_de_idade >= 18 and possui_carteira_de_trabalho == True)
print(maior_de_idade and possui_carteira_de_trabalho)
print(maior_de_idade < 18 and possui_carteira_de_trabalho == False)
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)