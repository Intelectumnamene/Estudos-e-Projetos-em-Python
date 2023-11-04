import sys
import os
from cx_Freeze import setup, Executable

#Definir o que deve ser incluído na pasta final
arquivos = ['web.ico', 'musicas/'] # caso haja um desses arquivos a barra / serve para adicionar tudo que está na pasta música.

# Saída de arquivos
configuracao = Executable(script = 'app.py', icon= 'web.ico')
# app.py o nome do programa
#icon como está atualazindo um arquivo de extensão .ico

#configurar o cs-freeze(delhes do programa)

setup(
    name ='Autorizador de login',
    version = '1.0'
    description = 'Este programa automatiza o login',
    author = 'Luiz'
    options = {'build_exe':{'include_files': arquivos}},
    executables = [configuracao]
)

#ir ao terminal e rodar o comando (python setup.py build)