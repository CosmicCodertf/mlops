import requests
url = 'http://127.0.0.1:5000/cotacao-completa/'


tamanho = float(input("Digite o tamanho da casa: "))
ano = int(input("Digite o ano de construção: "))
garagem = int(input("Digite o número de vagas na garagem: "))


dados = {
	"tamanho":tamanho,
	"ano":ano,
	"garagem":garagem
}

auth = requests.auth.HTTPBasicAuth('mrrobot', 'robot123')
response = requests.post(url, json=dados, auth=auth)

valor = response.json()

print (response.status_code)

print(valor)