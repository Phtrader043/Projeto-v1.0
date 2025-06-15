import streamlit as st
from signal_engine import gerar_sinal
from utils import carregar_historico, salvar_sinal, exibir_historico
from datetime import datetime
import pytz

# Configurações da página
st.set_page_config(page_title="Indicador GPT 1.0", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/loX5xBF.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📈 Indicador GPT 1.0 - Cripto & Forex")

st.sidebar.title("Configurações")
modo = st.sidebar.selectbox("Selecione o Modo:", ["Conservador", "Agressivo"])

# Botão para ativar IA
ativar_ia = st.sidebar.toggle("🚀 Ativar IA", value=False)

# Exibir histórico
st.subheader("📜 Histórico de Sinais")
exibir_historico()

# Loop para geração automática de sinais
if ativar_ia:
    st.success("✅ IA Ativada e Buscando Sinais...")
    sinal = gerar_sinal(modo)
    salvar_sinal(sinal)
    st.subheader("🔔 Novo Sinal Gerado")
    st.json(sinal)
else:
    st.warning("🚫 IA Desativada")
    
