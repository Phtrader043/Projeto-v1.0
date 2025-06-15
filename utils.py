import pandas as pd
import os

def carregar_historico():
    if not os.path.exists("historicos/sinais.csv"):
        return pd.DataFrame(columns=["Ativo", "Tipo", "Entrada", "Saída", "Tendência"])
    return pd.read_csv("historicos/sinais.csv")

def salvar_sinal(sinal):
    df = carregar_historico()
    df = pd.concat([df, pd.DataFrame([sinal])], ignore_index=True)
    df.to_csv("historicos/sinais.csv", index=False)

def exibir_historico():
    df = carregar_historico()
    if df.empty:
        st.info("Nenhum sinal gerado ainda.")
    else:
        st.table(df.tail(10))
        
