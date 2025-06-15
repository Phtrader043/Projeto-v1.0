import streamlit as st
import json
from datetime import datetime, timedelta


def horario_brasilia():
    agora = datetime.utcnow() - timedelta(hours=3)
    return int(agora.strftime('%M'))


def salvar_sinal(sinal):
    try:
        with open('historico.json', 'r') as f:
            historico = json.load(f)
    except:
        historico = []

    historico.append(sinal)
    with open('historico.json', 'w') as f:
        json.dump(historico, f)


def exibir_historico():
    try:
        with open('historico.json', 'r') as f:
            historico = json.load(f)
        st.subheader("📜 Histórico de Sinais")
        for item in historico[-10:][::-1]:
            st.info(f"""
            **Ativo:** {item['Ativo']}  
            **Tipo:** {item['Tipo']}  
            **Entrada:** {item['Entrada']}  
            **Saída:** {item['Saída']}  
            **Tendência:** {item['Tendência']}
            """)
    except:
        st.info("Nenhum sinal gerado ainda.")


def carregar_background(imagem):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{carregar_imagem_base64(imagem)}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def carregar_imagem_base64(imagem):
    import base64
    with open(imagem, "rb") as img:
        return base64.b64encode(img.read()).decode()
        
