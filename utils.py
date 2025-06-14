import streamlit as st

def carregar_imagem():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/Qf6uIuR.png");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
