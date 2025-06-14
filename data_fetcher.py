import requests

API_KEY_TWELVEDATA = "08665d12c4394cafad7e9a36f1bf3ba8"
API_KEY_CRYPTOCOMPARE = "02816cb2d68aafdda6b92cc525cdcaf663f780978c30d9e5429d6712a52cfdff"

def obter_dados():
    ativos = ["BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD"]
    dados = {}
    for ativo in ativos:
        candles = obter_candles(ativo)
        dados[ativo] = candles
    return dados

def obter_candles(ativo):
    symbol = ativo.replace("/", "")
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={API_KEY_TWELVEDATA}"
    r = requests.get(url)
    if r.status_code == 200 and "values" in r.json():
        return r.json()["values"]
    else:
        return []
