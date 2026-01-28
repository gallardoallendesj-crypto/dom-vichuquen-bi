import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración Pro
st.set_page_config(page_title="DOM Vichuquén BI", layout="wide")

# Estilo Vichuquén
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header { background: linear-gradient(135deg, #004d40 0%, #008080 100%); padding: 2rem; border-radius: 20px; color: white; margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏛️ DASHBOARD ELITE: Gestión Territorial Vichuquén</h1></div>', unsafe_allow_html=True)

# KPIs según tu reporte Excel
c1, c2, c3, c4 = st.columns(4)
c1.metric("Gestión Total", "1,304")
c2.metric("% Digitalización", "46%", help="Meta: 80%")
c3.metric("Certificados", "857")
c4.metric("Trámites", "447")

st.divider()

# Gráfico de Ranking TOP 5
st.subheader("🏆 Ranking TOP 5 de Trámites")
# Datos de tu Excel: CIP(415), Número(316), Edificación(197), Otros(157), Recepción(38)
df_rank = pd.DataFrame({
    'Trámite': ["CIP", "Número", "Edificación", "Otros", "Recepción"],
    'Total': [415, 316, 197, 157, 38]
})
fig = px.bar(df_rank, x='Total', y='Trámite', orientation='h', color_discrete_sequence=['#008080'])
st.plotly_chart(fig, use_container_width=True)
