from setuptools import setup, find_namespace_packages
from pathlib import Path

setup(
    name= 'pro-video',#nomefictício do pacote
    version= 1.0,
    description= 'Este pacote irá fornecer ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(),
    outhor = 'Luiz',
    outhor_email='Luizinho_2002@hotmail.com',
    keywords=['camera', 'video','processamento'],
    packages= find_packages()#instala todas as dependências que o pacote precisa.

)

#para publicar é preciso entrar no site pypi.org entrar com uma conta no site
#no terminal do VScode fazer a instalação dos pacotes- pip install setuptolls twine
#comando para deixar o pacote pronto para o pypi.org - python .\setup.py sdist
#gerará udois arquivos DIST arquivo no vscode para enviar para o pypi.org então digite o seguinte comando.
#  twine upload --repository-url https://upload.pypi.org/legacy /dist/*
#quando der enter vai pedir o usuário e senha 

