# Documentação do Código - Aplicação de Visualização de Dados COVID-19
Este é um script Python que utiliza a biblioteca Streamlit para criar uma aplicação web interativa para visualizar dados da COVID-19 no Brasil. A aplicação permite ao usuário escolher um estado e o tipo de informação que deseja visualizar, gerando um gráfico de linha interativo usando a biblioteca Plotly Express. Abaixo está a documentação detalhada do código.

# Bibliotecas Utilizadas
pandas: Utilizada para a manipulação e análise de dados.
plotly.express: Utilizada para criar visualizações interativas de dados.
streamlit: Utilizada para criar a interface web interativa.

#Leitura dos Dados
Os dados da COVID-19 são lidos a partir de um arquivo CSV chamado 'cases-brazil-states.csv' usando a função pd.read_csv(). Em seguida, as colunas do DataFrame são renomeadas para tornar os nomes mais amigáveis.

# Seleção do Estado
O usuário pode selecionar o estado que deseja visualizar a partir de uma lista de estados únicos presentes no DataFrame. Isso é feito usando st.sidebar.selectbox() do Streamlit.

# Seleção da Coluna
O usuário também pode escolher o tipo de informação que deseja visualizar, como novos óbitos, novos casos, óbitos por 100 mil habitantes ou casos por 100 mil habitantes. As opções são apresentadas em um menu suspenso no sidebar.

# Filtragem dos Dados
Os dados do estado selecionado são filtrados a partir do DataFrame original para que apenas as informações relacionadas ao estado escolhido sejam mantidas. Isso é feito usando a linha df = df[df['state'] == state].

# Criação do Gráfico
Um gráfico de linha interativo é criado usando a biblioteca Plotly Express. O eixo x representa a data e o eixo y representa a métrica selecionada pelo usuário. O título do gráfico é composto pelo nome da métrica e o nome do estado selecionado.

# Interface Web
O título da aplicação e uma breve descrição são exibidos acima do gráfico.
O gráfico gerado é exibido no corpo principal da aplicação usando st.plotly_chart().
Uma legenda é exibida abaixo do gráfico para informar ao usuário de onde os dados foram obtidos.
Execução da Aplicação
A aplicação Streamlit pode ser executada no terminal com o comando streamlit run covid.py, onde covid.py é o nome do arquivo que contém o código.

# Fonte de Dados
Os dados utilizados na aplicação foram obtidos do seguinte repositório no GitHub: https://github.com/wcota/covid19br

# Conclusão
Este código cria uma aplicação web interativa para visualizar dados da COVID-19 no Brasil de forma simples e amigável, permitindo ao usuário explorar diferentes métricas e estados. A documentação fornece uma visão geral das principais funcionalidades e bibliotecas utilizadas no código.
