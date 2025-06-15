import requests

API_KEY = "cd52d4f5c5924063a7af0070445d2a3b"
ATIVOS = ["BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD"]

def obter_dados():
    dados = {}
    for ativo in ATIVOS:
        url = f"https://api.twelvedata.com/time_series?symbol={ativo}&interval=1min&apikey={API_KEY}&outputsize=20"
        response = requests.get(url)
        if response.status_code == 200:
            serie = response.json().get('values')
            if serie:
                dados[ativo] = serie
    return dados
    
