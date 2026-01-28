import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página profesional
st.set_page_config(page_title="DOM Vichuquén | Reporte MINVU", layout="wide")

# Estilo visual institucional
st.markdown("""
    <style>
    .report-banner {
        background: linear-gradient(135deg, #004d40 0%, #00695c 100%);
        color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="report-banner"><h1>🏛️ DIAGNÓSTICO GESTIÓN DOM VICHUQUÉN</h1><p>Cumplimiento Ley 21.180 - Transformación Digital</p></div>', unsafe_allow_html=True)

# KPIs basados en tu Excel de la imagen
c1, c2, c3, c4 = st.columns(4)
c1.metric("Gestión Total", "1,304", help="Total solicitudes ingresadas") #
c2.metric("Digitalización", "46%", delta="-34% vs Meta 80%") #
c3.metric("Certificados", "857") #
c4.metric("Trámites", "447") #

st.divider()

# Ranking TOP 5 según tu tabla de Excel
st.subheader("🏆 Ranking TOP 5 de Trámites")
datos_ranking = pd.DataFrame({
    'Trámite': ["CIP", "Cert. Número", "Edificación", "Otros", "Recepción"], #
    'Total': [415, 316, 197, 157, 38] #
})
fig = px.bar(datos_ranking, x='Total', y='Trámite', orientation='h', color_discrete_sequence=['#008080'])
st.plotly_chart(fig, use_container_width=True)
