import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

with st.container():
    st.subheader ("DashBoard Exibição de faturamento")


df = pd.read_csv("Vendas_Produtos.csv", sep=";", decimal=",")
df["Data"] = pd.to_datetime(df["Data"])
df=df.sort_values("Data")


df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique())



df_filtered = df[df["Month"] == month]

coluna1, coluna2 = st.columns(2)
coluna3, coluna4 = st.columns(2)



figure_data = px.bar(df_filtered, x="Data", y="Total", color="Cidade", title="Faturamento no Dia")
coluna1.plotly_chart(figure_data, use_container_width=True)

total_cidade = df_filtered.groupby("Cidade")[["Total"]].sum().reset_index()
fig_city = px.bar(total_cidade, x="Cidade", y="Total",
                   title="Faturamento Por Filial    ")
coluna2.plotly_chart(fig_city, use_container_width=True)


figure_produto = px.bar(df_filtered, x="Quantidade", y="Produtos", 
                  color="Cidade", title="Faturamento por Quantidade de Produtos",
                  orientation="h")  
coluna3.plotly_chart(figure_produto, use_container_width=True)

figure_tipo_pagamento = px.pie(df_filtered, values="Total", names="Forma de Pagamento",
                   title="Faturamento por tipo de pagamento")
coluna4.plotly_chart(figure_tipo_pagamento, use_container_width=True)



