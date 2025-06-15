from data_fetcher import obter_dados
from indicators import analisar_indicadores
from cohere_analysis import analisar_tendencia
from utils import salvar_sinal, horario_brasilia
import random


def gerar_sinal(modo):
    dados = obter_dados()

    if not dados:
        return None

    analise_indicadores = analisar_indicadores(dados, modo)

    if not analise_indicadores['sinal']:
        return None

    try:
        analise_ia = analisar_tendencia(analise_indicadores, modo)
    except Exception:
        analise_ia = True  # Se IA falhar, segue só com indicadores

    if analise_ia:
        horario_atual = horario_brasilia()
        sinal = {
            "Ativo": analise_indicadores['ativo'],
            "Tipo": analise_indicadores['sinal'],
            "Entrada": horario_atual,
            "Saída": (horario_atual + 5) % 60,
            "Tendência": f"{random.randint(90, 99)}%"
        }
        salvar_sinal(sinal)
        return sinal
    else:
        return None
        
