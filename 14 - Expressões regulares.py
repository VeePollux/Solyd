import re
import requests

requisicao = requests.get("https://presuntovegetariano.com.br/contato/")

padrao = re.findall(r'[\w\.-]+@[\w\-]+\.[\w\.-]+', requisicao.text)  #RAW string 

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado.")