import requests
import random

API_KEY_TWELVE = "cd52d4f5c5924063a7af0070445d2a3b"
API_KEY_CRYPTOCOMPARE = "02816cb2d68aafdda6b92cc525cdcaf663f780978c30d9e5429d6712a52cfdff"

# Lista de ativos (pares cripto + forex)
ativos = [
    "BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD",
    "USD/CAD", "USD/CHF", "NZD/USD", "XAU/USD", "XAG/USD"
]

def obter_dados():
    ativo = random.choice(ativos)

    url = f"https://api.twelvedata.com/time_series?symbol={ativo}&interval=1min&outputsize=30&apikey={API_KEY_TWELVE}"
    r = requests.get(url)
    dados = r.json()

    candles = dados.get("values", [])

    indicadores = {
        "rsi": consultar_indicador("rsi", ativo),
        "macd": consultar_indicador("macd", ativo),
        "ema": consultar_indicador("ema", ativo),
        "adx": consultar_indicador("adx", ativo),
        "stochastic": consultar_indicador("stoch", ativo),
        "bbands": consultar_indicador("bbands", ativo)
    }

    return {
        "ativo": ativo,
        "candles": candles,
        "indicadores": indicadores
    }

def consultar_indicador(indicador, ativo):
    url = f"https://api.twelvedata.com/{indicador}?symbol={ativo}&interval=1min&apikey={API_KEY_TWELVE}"
    r = requests.get(url)
    return r.json()
    
