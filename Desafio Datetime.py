from datetime import datetime
data_de_aniversário = datetime(2023,3,21)
resultado = datetime.now() - data_de_aniversário
print("Faltam {} dias para o seu aniversário!".format(resultado))

