
from cohere_analysis import analisar_tendencia
from data_fetcher import obter_dados

def gerar_sinal(modo):
    dados = obter_dados()
    analise = analisar_tendencia(dados, modo)
    return analise
