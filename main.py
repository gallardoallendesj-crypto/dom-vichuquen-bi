import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURACIÓN ESTRUCTURAL ---
st.set_page_config(page_title="DOM Vichuquén | Reporte MINVU", layout="wide")

# --- ESTILO INSTITUCIONAL (Verde Vichuquén #004d40) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .report-banner {
        background: linear-gradient(135deg, #004d40 0%, #00695c 100%);
        color: white; padding: 2.5rem; border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 2rem;
    }
    .metric-card {
        background: white; padding: 20px; border-radius: 12px;
        border-top: 5px solid #008080; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO MINVU ---
st.markdown("""
    <div class="report-banner">
        <h1>🏛️ DIAGNÓSTICO DE GESTIÓN TERRITORIAL</h1>
        <p>Municipalidad de Vichuquén | Cumplimiento Ley de Transformación Digital</p>
    </div>
    """, unsafe_allow_html=True)

# --- BLOQUE 1: INDICADORES DE DIGITALIZACIÓN (KPI MINVU) ---
# Datos basados en tu reporte: 1304 solicitudes totales
st.subheader("📊 Indicadores de Desempeño (KPIs)")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Gestión Total", "1,304", help="Suma de ingresos DOMEL y Presenciales")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Tasa Digitalización", "46%", delta="-34% vs Meta MINVU (80%)")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Certificados", "857", help="Incluye CIP, Número y otros certificados")
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Permisos y Trámites", "447", help="Ingresos de Edificación y trámites complejos")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- BLOQUE 2: RANKING Y ADMISIBILIDAD ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🏆 Ranking TOP 5 de Demanda Territorial")
    # Datos Ranking: CIP(415), Número(316), Edificación(197), Otros(157), Recepción(38)
    df_rank = pd.DataFrame({
        'Trámite': ["Informaciones Previas (CIP)", "Certificado de Número", "Permiso Edificación", "Otros (Varios)", "Recepción Definitiva"],
        'Volumen': [415, 316, 197, 157, 38],
        'Digitalización': ["46%", "50%", "55%", "35%", "21%"]
    })
    
    fig_rank = px.bar(df_rank, x='Volumen', y='Trámite', orientation='h',
                     color='Volumen', color_continuous_scale='Greens',
                     text='Digitalización')
    fig_rank.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_rank, use_container_width=True)

with col_right:
    st.subheader("⚖️ Estado de Admisibilidad")
    # Proporción: 304 Admitidas vs 296 No Admisibles
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Admitidas', 'No Admisibles'],
        values=[304, 296],
        hole=.5,
        marker_colors=['#004d40', '#CD5C5C']
    )])
    fig_pie.update_layout(height=400, showlegend=True)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- BLOQUE 3: ESTRATEGIA CERO PAPEL ---
with st.expander("📝 Nota Técnica: Ley 21.180"):
    st.write("""
        Este dashboard visualiza la brecha de digitalización actual. 
        Para cumplir con los requerimientos de la DOM en Línea, se debe priorizar 
        la digitalización de los procesos de **Recepción Definitiva**, 
        que actualmente presentan la tasa más baja de adopción digital (21%).
    """)
