import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config( # Cria o titulo e o layout da página da aplicação
    page_title="Classificação de Veículos",
    layout="wide"
)

@st.cache_data #deixa os dados da aplicação em cache e não precisa carregar a aplicação toda vez que atualizar
def load_data_and_model(): #carrega os dados e os modelos de predissão
    carros = pd.read_csv("car.csv", sep=",")
    encoder = OrdinalEncoder()

    for col in carros.columns.drop('class'): # vai percorrer carros mas removendo a coluna class
        carros[col] = carros[col].astype('category') #todas as colunas exeto class vai ser categorico

    X_encoded = encoder.fit_transform(carros.drop('class', axis=1)) #aplicado o encoder na variavel X

    y = carros['class'].astype('category').cat.codes #faz uma transformação para valores categoricos

    #divide os dados para treinar o modelo e aplicar a prova para teste utilizando 30%
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

    modelo = CategoricalNB()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred) #pedi para ele prever a classe acuracia é o percentual de acerto

    return encoder, modelo, acuracia, carros

encoder, modelo, acuracia, carros = load_data_and_model()

st.title('Previsão de Qualidade de Veículo') #titulo
st.write(f'Acurácia do Modelo: {acuracia:.2f}')

input_features = [
        st.selectbox('Preço:', carros['buying'].unique()), #vai selecionar um valor único
        st.selectbox('Manutenção:', carros['maint'].unique()),
        st.selectbox('Portas:', carros['doors'].unique()),
        st.selectbox('Capacidade de Passageiros:', carros['persons'].unique()),
        st.selectbox('Porta Malas:', carros['lug_boot'].unique()),
        st.selectbox('Segurança:', carros['safety'].unique()),
    ]

if st.button('Processar'):
    # criando um dataframe de input com o nome das colunas corretas sem o class
    input_df = pd.DataFrame([input_features], columns=carros.columns.drop('class'))
    input_encoder = encoder.transform(input_df) #fazendo a transformação categorica com os dados que o usuário entrou
    predict_encoded = modelo.predict(input_encoder)
    previsao = carros['class'].astype('category').cat.categories[predict_encoded][0] #previsao final com um valor que o usuário entenda
    st.header(f'Resultado da Previsão: {previsao}')