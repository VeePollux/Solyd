import requests
import json

cidade = input("Escreva a cidade:")

requisicao1 = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + cidade + "&appid=adaa41452a1b17c9c5d4c0a4536c4cf6")
dicionario = json.loads(requisicao1.text)
print("###Requisição Geografica###")
print(dicionario)
latitude = dicionario[0]["lat"]
longitude = dicionario[0]["lon"]
requisicao2 = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=adaa41452a1b17c9c5d4c0a4536c4cf6")


requisicao3 = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ cidade + "&units=metric&appid=adaa41452a1b17c9c5d4c0a4536c4cf6")

req2 =json.loads(requisicao2.text)
req3 = json.loads(requisicao3.text)
print("\n###Condições do tempo###")
print(req2["weather"][0]["main"])
print(req3["weather"][0]["main"])