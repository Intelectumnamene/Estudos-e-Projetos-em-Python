import json

carros_json = '{"Marca":"Honda","Modelo":"HRV","Cor":"Prata"}'

carros = json.loads(carros_json)

for k,v in carros.items():
    print(k + "-" + v)


#print(carros["Marcas"])

#for x in carros:
    #print(x)

#for x in carros.items():
#    print(x)
#for k, v in carros.values():
#print(k,v)


