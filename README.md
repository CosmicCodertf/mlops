# mlops
Iniciando com machine learning, disponibilizando em flask uma api de análise preditiva do preço de casas, através dos variáveis "tamanho", "ano", "garagem".

# Para executar o projeto, instale as dependências com:
pip install -r requirements.txt

# Crie e ative o ambiente virtual:
python -m venv nome_do_ambiente

# Ativando em Windows:
nome_do_ambiente\Scripts\activate

# Ativando em Linux:
sorce nome_do_ambiente/bin/activate

# O diretório treinamento-modelo possui a lógica do modelo, com a base de dados casas.csv.
Após a execução, é gerado um arquivo de modelo modelo-serializado.sav tornando o modelo um objeto para a análise.
O mesmo arquivo já existe no dir apis para execução da análise.

# Subindo o ambiente em Flask:
python apis/main.py, logs estão sendo enviados para o arquivo flask.log
