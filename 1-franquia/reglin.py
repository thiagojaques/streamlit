import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title('Previsão Inicial de Custo para franquia') #titulo da aplicação

dados = pd.read_csv("slr12.csv", sep=";") # Carregar os dados do aquivo 'slr12.csv' e indica o separador ';'

X = dados[['FrqAnual']] # geralmente o 'x' é usado para a variável independente [[ '' ]] indica que pode ter múltiplas variáveis
y = dados['CusInic'] # variável dependente

modelo = LinearRegression().fit(X, y) # 'fit' é o método que treina o machine learning

col1, col2 = st.columns(2) # cria colunas para mostrar na aplicação

with col1: # cria uma coluna mostrando os dados carregados do arquivo 'slr12.csv'
    st.header('Dados')
    st.table(dados.head(10))

with col2: # criar o gráfico de dispersão com o matplotlib
    st.header('Gráfico de Dispersão')
    fig, ax = plt.subplots() # o elemento fig representa todo o gráfico e o ax representa um subplot ou subgráfico que será impresso
    ax.scatter(X, y, color='blue')
    ax.plot(X, modelo.predict(X), color='red') # cria a linha de regressão ou de maior ajuste
    st.pyplot(fig)

st.header('Valor Anual da Franquia:') # Titulo da entrada de dados 
novo_valor = st.number_input('Insira Novo Valor', min_value=1.0, max_value=999999999999.0, value=1500.0, step=1.0)
processar = st.button('Processar')

if processar:
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = modelo.predict(dados_novo_valor)
    st.header(f'Previsão de Custo Inicial R${prev[0]:2f}')