import random
from pprint import pprint

sorteios = ['sorteio1','sorteio2','sorteio3']
participantes = ['Joel','Jessica','Maria','Cris','Larissa','Rafael','Marcus','John']

pprint({sorteio: random.choice(participantes)for sorteio in sorteios})

grupos = ['grupo 1','grupo 2','grupo 3']

pprint({grupo:[random.randint(1,101)for i in range(5)] for grupo in grupos})