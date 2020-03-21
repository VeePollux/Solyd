import requests   #Se querer trabalhar mais com pegar paginas etc a melhor biblioteca é a Beautiful Soup 4 ou BS4
requisicao = requests.get("https://solyd.com.br")
print(requisicao)
print(type(requisicao))
print(requisicao.status_code)
print(requisicao.text)


cabecalho = {"User-agent": "Windowns 21",
             "Referer" : "https://google.com"}
variavel = None
try:
    variavel = requests.get("https://g1.com.br")
    print(variavel.text)
except Exception as e:
    print("Requisição deu erro:", e)
print(variavel)

meus_cookies = {"Ultima visita" : "10-10-2010"}
dados = {"username": "Pollux",
         "password" : "pollux123"}


vari = None
try:
    requi = requests.get("https://putsreq.com/igz2xaIGxSy2Q1eIG6RV",
                         headers=cabecalho,
                         cookies = meus_cookies,
                         data = dados)
    vari = requi.text
except Exception as er:
    print("Requisição deu erro:", er)
print(vari)