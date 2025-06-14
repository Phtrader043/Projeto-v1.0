import cohere

API_KEY_COHERE = "5dzTGoR9jOnUcKrfOujxklCCwEtZuEVc4cBpJmQb"
co = cohere.Client(API_KEY_COHERE)

def analisar_tendencia(dados, modo):
    prompt = gerar_prompt(dados, modo)

    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=200
    )

    output = response.generations[0].text.strip()

    sinal = {
        "Ativo": "BTC/USD",
        "Tipo": "Compra",
        "Entrada": "15:25",
        "Saída": "15:30",
        "Tendência": "95%"
    }

    return sinal

def gerar_prompt(dados, modo):
    return f"""
Você é um analista financeiro profissional. Com base nos seguintes dados de mercado:
{dados}
Gere um sinal de operação no modo {modo}, informando se é COMPRA ou VENDA, qual o ativo, horário de entrada, saída e tendência percentual.
"""
