import random
from pprint import pprint
#pprint({i: i for i in range(20)})

produtos = ['produto1', 'produto2','produto3','produto4','produto5']
#pprint({produto: 1 for produto in produtos})

# pprint({produto:[0 for i in range(5)] for produto in produtos})
# pprint({produto: [i * 2 for i in range(5)] for produto in produtos})

pprint({produto:[random.randint(1000, 15000)for i in range(5)]for produto in produtos})