import requests
import argparse
from requests.auth import HTTPBasicAuth

def main(tamanho, ano, garagem, username, password):

    url = 'http://127.0.0.1:5000/cotacao-completa/'

    dados = {
   "tamanho": float(tamanho), 
   "ano": int(ano),
   "garagem": int(garagem)
}

    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.post(url, json=dados, auth=auth)

    valor = response.json()

    print(valor)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enviar dados para a API Flask.')
    parser.add_argument('--tamanho', required=True, help='Tamanho da casa')
    parser.add_argument('--ano', required=True, help='Ano de construção')
    parser.add_argument('--garagem', required=True, help='Número de vagas na garagem')

    args = parser.parse_args()
    main(args.tamanho, args.ano, args.garagem)
