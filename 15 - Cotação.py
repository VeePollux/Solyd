import requests
import json

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

cotacao = json.loads(requisicao.text)

print("###COTAÇÃO###")
print("Dólar:", cotacao["USDBRL"]["high"])
print("Euro:", cotacao["EURBRL"]["high"])
print("Bitcoin:", cotacao["BTCBRL"]["high"])