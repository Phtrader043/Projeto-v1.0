import streamlit as st
from signal_engine import gerar_sinal
from utils import carregar_imagem

st.set_page_config(page_title="Indicador GPT - Cripto & Forex", layout="wide")

# Fundo personalizado
carregar_imagem()

st.title("🧠 Indicador GPT - Cripto & Forex")

modo = st.selectbox("Selecione o Modo de Operação:", ["Conservador", "Agressivo"])

if st.button("🚀 Ativar IA"):
    with st.spinner("Analisando mercado e gerando sinal..."):
        sinal = gerar_sinal(modo)
        st.success("✅ Sinal Gerado")
        st.json(sinal)
