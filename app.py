import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Educação",
    layout="wide"
)

st.title("Dashboard de Educação")

st.write("""
Este dashboard apresenta dados do Censo Escolar 2025.
O objetivo é analisar a distribuição das matrículas na educação básica.
""")

st.info("""
Fonte dos dados: Censo Escolar 2025 — INEP.
""")

arquivo = "Tabela_Matricula_2025_V2.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="latin1"
)

st.subheader("Visualização dos dados")

st.dataframe(df.head())

col1, col2 = st.columns(2)

col1.metric(
    "Quantidade de registros",
    df.shape[0]
)

col2.metric(
    "Quantidade de colunas",
    df.shape[1]
)

st.subheader("Matrículas por estado")

matriculas_estado = (
    df.groupby("NO_UF")["QT_MAT_BAS"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_estado = px.bar(
    matriculas_estado,
    x="NO_UF",
    y="QT_MAT_BAS",
    title="Número de matrículas por estado",
    labels={
        "NO_UF": "Estado",
        "QT_MAT_BAS": "Matrículas"
    }
)

st.plotly_chart(
    fig_estado,
    use_container_width=True
)

st.subheader("Matrículas por etapa de ensino")

etapas = pd.DataFrame({
    "Etapa": [
        "Educação Infantil",
        "Ensino Fundamental",
        "Ensino Médio",
        "Educação Profissional",
        "EJA"
    ],
    "Matrículas": [
        df["QT_MAT_INF"].sum(),
        df["QT_MAT_FUND"].sum(),
        df["QT_MAT_MED"].sum(),
        df["QT_MAT_PROF"].sum(),
        df["QT_MAT_EJA"].sum()
    ]
})

fig_etapas = px.bar(
    etapas,
    x="Etapa",
    y="Matrículas",
    title="Matrículas por etapa de ensino",
    labels={
        "Etapa": "Etapa de ensino",
        "Matrículas": "Quantidade de matrículas"
    }
)

st.plotly_chart(
    fig_etapas,
    use_container_width=True
)