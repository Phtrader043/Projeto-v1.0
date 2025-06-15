import streamlit as st
from signal_engine import gerar_sinal
from utils import exibir_historico, carregar_background
import time

# Carregar background
carregar_background("assets/background.png")

st.title("💹 Indicador GPT 1.0 - Forex e Cripto")

modo = st.radio("Selecione o modo de operação:", ("Conservador", "Agressivo"))
ativar = st.toggle("🚀 Ativar IA")

st.subheader("📊 Sinais Gerados")

if ativar:
    while True:
        with st.spinner('Buscando sinal...'):
            sinal = gerar_sinal(modo)
            if sinal:
                st.success(f"""
                **Ativo:** {sinal['Ativo']}
                **Tipo:** {sinal['Tipo']}
                **Entrada:** {sinal['Entrada']}
                **Saída:** {sinal['Saída']}
                **Tendência:** {sinal['Tendência']}
                """)
            else:
                st.warning("Nenhum sinal confiável encontrado no momento.")
            exibir_historico()
            time.sleep(300)  # Espera 5 minutos
else:
    st.info("IA Desativada. Clique em 'Ativar IA' para iniciar.")
    exibir_historico()
            
