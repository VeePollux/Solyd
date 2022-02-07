import requests
import json
req = None

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=26bd6fd8&t=" + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro")
        return None

def detalhes(filme):
    print("Título:", filme["Title"])
    print("Ano:", filme["Year"])
    print("Diretor:", filme["Director"])
    print("Atores:", filme["Actors"])
    print("Nota:", filme["imdbRating"])
    print("Prêmios:", filme["Awards"])
    print("Capa:", filme["Poster"])

sair = False

while not sair:
    op = input("Digite nome do filme ou sair:")
    if op == "sair":
        sair = True
        print("Saindo...")
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print("Filme não encontrado.")
        else:
            detalhes(filme)
