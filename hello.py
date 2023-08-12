#!/usr/bin/env python3

# Espaço de documentação

"""Hello Línguas

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument `--lang`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

# Metadados
__version__ = "0.0.1"
__author__ = "Lara Santos"
__license__ = "Unlicense"

import os # lê variáveis de ambiente
# lang = "pt_BR.utf8"; lang[:5] pega os primeiros cinco caracteres
# lang.split(".") divide pt_BR e utf8; lang.split[0] = pt_BR e lang.split[1] = utf8

# Este programa imprime hello world

current_language = os.getenv("LANG", "en_US")[:5]
# snake case
# Pascal Case CurrentLanguage

msg = "Hello World"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg) #built-in