import json

marcas_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""

data = json.loads(marcas_json)
print(data["name"])

with open('marcas_json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(data, arquivo_json)

with open('marcas_json', encoding='utf-8') as arquivo_json:
    dicionario_marcas_json = json.load(arquivo_json)
    print(dicionario_marcas_json["name"])
    