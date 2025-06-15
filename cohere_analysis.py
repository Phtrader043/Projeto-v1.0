import cohere

API_COHERE = "lGzCPrGBMfOjqX9h2xel4ZZb6G7QlE6ehKRhZslG"
co = cohere.Client(API_COHERE)


def analisar_tendencia(analise, modo):
    prompt = f"""
    Você é um especialista em Forex e Cripto. Analise a seguinte situação:
    Ativo: {analise['ativo']}
    Sinal: {analise['sinal']}
    Modo: {modo}
    Isso parece uma oportunidade segura? Responda com 'Sim' ou 'Não'.
    """

    resposta = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=10
    )
    texto = resposta.generations[0].text.lower()
    return 'sim' in texto
    
