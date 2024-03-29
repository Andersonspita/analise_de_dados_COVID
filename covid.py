import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit run covid.py

#LENDO O DATASET
df = pd.read_csv('cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

#SELEÇÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual o estado', estados)


#SELEÇÃO DA COLUNA
#column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual o tipo de informação?', colunas)


#SELEÇÃO DAS LINHAS QUE PERTENCEM AO ESTADO
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x': 0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação o usuário tem opção de escolher o estado e o tipo de informação para mostrar o gráfico. Use o menu lateral para alterar a amostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os daddos foram obtidos a partir do site : https://github.com/wcota/covid19br')
