from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split 

df = pd.read_csv('casas.csv')
colunas = ['tamanho', 'ano', 'garagem']

x = df.drop('preco', axis=1)
y = df['preco']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

pickle.dump(modelo, open('modelo-serializado1.sav', 'wb'))
