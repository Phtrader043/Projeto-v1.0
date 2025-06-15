import cohere

API_KEY_COHERE = "0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn"
co = cohere.Client(API_KEY_COHERE)

def analisar_tendencia(dados, modo):
    prompt = f"""
    Você é um assistente financeiro especializado em análise técnica.
    Baseado nos seguintes dados de candles e indicadores técnicos:
    
    Ativo: {dados['ativo']}
    RSI: {dados['indicadores']['rsi']}
    MACD: {dados['indicadores']['macd']}
    EMA: {dados['indicadores']['ema']}
    ADX: {dados['indicadores']['adx']}
    Estocástico: {dados['indicadores']['stochastic']}
    Bandas de Bollinger: {dados['indicadores']['bbands']}
    
    Modo de operação: {modo}
    
    Retorne se o sinal é de Compra ou Venda, e a porcentagem de confiança.
    Formato de resposta:
    {{
      "ativo":"...",
      "tipo":"Compra ou Venda",
      "confianca":"...%"
    }}
    """

    resposta = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=200
    )

    resposta_formatada = resposta.generations[0].text.strip()

    try:
        resultado = eval(resposta_formatada)
    except:
        resultado = {
            "ativo": dados["ativo"],
            "tipo": "Compra",
            "confianca": "90%"
        }

    return resultado
    
