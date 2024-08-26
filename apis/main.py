from flask import Flask, request, jsonify, g
from flask_basicauth import BasicAuth
from textblob import TextBlob
from googletrans import Translator ## necessário para versão mais recente do textblob
from sklearn.linear_model import LinearRegression
import pickle
import logging

app = Flask(__name__)

# Configuração do registro de log
logging.basicConfig(filename='flask.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Middleware para logar requisições e respostas
@app.before_request
def before_request():
    g.request_start_time = logging.getLogger().handlers[0].formatter.formatTime(logging.LogRecord('', '', '', '', '', '', '', '', '')) 
    g.request_start_time = request.path

@app.after_request
def after_request(response):
    logger = logging.getLogger()
    logger.info('%s %s %s %s %s', 
                request.remote_addr, 
                request.method, 
                request.scheme, 
                request.full_path, 
                response.status)
    return response


modelo = pickle.load(open('modelo-serializado.sav', 'rb')) # inputando o modelo-serializado construído no arquivo treinamento-do-modelo.py

colunas = ['tamanho', 'ano', 'garagem'] # Variáveis analisadas

app.config['BASIC_AUTH_USERNAME'] = 'mrrobot' #Inserindo uma autenticação básica
app.config['BASIC_AUTH_PASSWORD'] = 'robot123'

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required #tornando a autenticação obrigatória
def home():
    return "Minha primeira API."

@app.route('/sentimento/<frase>') # Endpoint da análise de sentimento
def sentimento(frase):
    translator = Translator()  # Cria uma instância do Translator sem parâmetros
    translated = translator.translate(frase, src='pt', dest='en')  # Traduza a frase
    tb = TextBlob(translated.text)  # Cria um TextBlob com o texto traduzido
    polaridade = tb.sentiment.polarity  # Obtém a polaridade do sentimento
    return "Polaridade: {}".format(polaridade)
    

@app.route('/cotacao-completa/', methods=['POST']) # Endpoint análise preditiva precos de casas
@basic_auth.required
def cotacao():
	dados = request.get_json()
	dados_input = [dados[col] for col in colunas]
	preco = modelo.predict([dados_input])
	return jsonify(preco=preco[0])

if __name__ == "__main__":
    app.run(debug=True)

