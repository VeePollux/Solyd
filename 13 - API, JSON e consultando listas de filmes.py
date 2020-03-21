import requests
req = None

try:
    req = requests.get("http://www.omdbapi.com/?t=The+Phantom+of+the+opera")
    print(req)
except:
    print("Erro")
    exit()

