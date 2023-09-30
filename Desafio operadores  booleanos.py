possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

print ((possui_passaporte and passagem_comprada )and not menor_de_idade)

print((possui_passaporte or passagem_comprada) and not menor_de_idade)

print((not possui_passaporte or not passagem_comprada) and menor_de_idade)

print(possui_passaporte and passagem_comprada or menor_de_idade)