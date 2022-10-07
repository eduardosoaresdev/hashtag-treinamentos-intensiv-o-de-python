#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[22]:


import pandas as pd

# Passo 1: Importar as bases de dados da empresa
tabela = pd.read_csv('telecom_users.csv')


# Passo 2: Visualizar as bases de dados
# -------- Entender quais as informações a gente tem
# -------- Descobrir as cagadas da base de dados

# axis é o eixo
# axis = 0 -> linha
# axis = 1 -> Coluna
tabela = tabela.drop('Unnamed: 0', axis=1)
display(tabela)


# In[23]:


# Passo 3: Tratamento de Dados

# valores são reconhecidos da forma errada
# errors='coerce' em caso de erro ele força o comando, caso haja texto no campo que estou
# convertendo para numérico
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# valores vazios
# colunas completamente vazias 
tabela = tabela.dropna(how='all', axis=1) # está deletando a coluna com todos os campos vazios

# linhas com pelo menos 1 valor vazio
tabela = tabela.dropna(how='any', axis=0) # está deletando as linhas com qualquer valor vazio

print(tabela.info())


# In[24]:


# Passo 4: Análise inicial do cenário (entender comoe stão os cancelamentos)

print(tabela['Churn'].value_counts()) # conta a quantidade de cada valor
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # mostra o % de cada valor
# o normalize calcula o % e o .map formata o resultado


# In[25]:


# Passo 5: Análise completa (entender o motivo do cancelamento)
# Churn = cancelamento

import plotly.express as px

for coluna in tabela.columns:
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
    # exibir o gráfico
    grafico.show()


# In[26]:


get_ipython().system('pip install plotly')


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# - Clientes com contrato mensal tem MUITO mais chance de cancelar:
#     - Podemos fazer promoções para o cliente ir para o contrato anual
#     
# - Familias maiores tendem a cancelar menos do que famílias menores
#     - Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
#     
# - MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito
#     - A primeira experiência do cliente na operadora pode ser ruim
#     - Talvez a captação de clientes tá trazendo clientes desqualificados
#     - Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
#     
# - QUanto mais serviços o cara tem, menos chance dele cancelar
#     - podemos fazer promoções com mais serviços pro cliente
#     
# - Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem
#     - Agir sobre a fibra
#     
# - Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento
