import json

carros = {"Marca":"Honda",
               "Modelo":"HRV",
               "Cor":"Prata"}

carros_json = json.dumps(carros)

print(carros_json)
