#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibi a mensagem
correspondente

Como usar:

Tenha a variavel LANG devidamente configurada ex:

        export LANG=pt_BR

Execulcao:

        python3 hello.py
        ou
        ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Leonardo Relva"
__license__ = "Unlicense"

import os

name = os.getenv('LOGNAME') # Pega os dados ambiente (env) do LOGNAME
print(f"NAME: {name}")

current_language = os.getenv('LANG')[:5] # Pega os primeiro 5 digitos do LANG
print(current_language)

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hole, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)
