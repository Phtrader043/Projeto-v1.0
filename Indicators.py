import pandas as pd
import numpy as np


def analisar_indicadores(dados, modo):
    for ativo, serie in dados.items():
        df = pd.DataFrame(serie).astype(float).iloc[::-1]
        df['ema'] = df['close'].ewm(span=10).mean()
        df['rsi'] = calcular_rsi(df['close'])
        df['macd'] = df['close'].ewm(span=12).mean() - df['close'].ewm(span=26).mean()

        condicao_compra = (
            df['close'].iloc[-1] > df['ema'].iloc[-1]
            and df['rsi'].iloc[-1] < 70
            and df['macd'].iloc[-1] > 0
        )
        condicao_venda = (
            df['close'].iloc[-1] < df['ema'].iloc[-1]
            and df['rsi'].iloc[-1] > 30
            and df['macd'].iloc[-1] < 0
        )

        if modo == "Conservador":
            if condicao_compra:
                return {'ativo': ativo, 'sinal': 'Compra'}
            if condicao_venda:
                return {'ativo': ativo, 'sinal': 'Venda'}
        else:
            if condicao_compra or condicao_venda:
                sinal = 'Compra' if condicao_compra else 'Venda'
                return {'ativo': ativo, 'sinal': sinal}

    return {'ativo': None, 'sinal': None}


def calcular_rsi(series, periodo=14):
    delta = series.diff()
    ganho = delta.clip(lower=0).fillna(0)
    perda = -delta.clip(upper=0).fillna(0)

    media_ganho = ganho.rolling(window=periodo).mean()
    media_perda = perda.rolling(window=periodo).mean()

    rs = media_ganho / media_perda
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)
