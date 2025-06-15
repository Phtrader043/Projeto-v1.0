from data_fetcher import obter_dados
from cohere_analysis import analisar_tendencia
from datetime import datetime, timedelta
import pytz

def gerar_sinal(modo):
    dados = obter_dados()

    analise = analisar_tendencia(dados, modo)

    agora = datetime.now(pytz.timezone('America/Sao_Paulo'))
    entrada = (agora + timedelta(minutes=2)).strftime("%H:%M")
    saida = (agora + timedelta(minutes=7)).strftime("%H:%M")

    sinal = {
        "Ativo": analise["ativo"],
        "Tipo": analise["tipo"],
        "Entrada": entrada,
        "Saída": saida,
        "Tendência": analise["confianca"]
    }

    return sinal
    
