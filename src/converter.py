"""
Простой конвертер валют
"""

# Курсы валют (упрощенные для демо)
RATES = {
    'USD': 1.0,      # базовая валюта
    'EUR': 0.85,     # 1 USD = 0.85 EUR
    'RUB': 75.0,     # 1 USD = 75 RUB
    'GBP': 0.73,     # 1 USD = 0.73 GBP
}

def convert_currency(amount, from_currency, to_currency):
    """
    Конвертирует валюту
    
    Args:
        amount (float): Сумма для конвертации
        from_currency (str): Исходная валюта
        to_currency (str): Целевая валюта
    
    Returns:
        float: Конвертированная сумма
    """
    if from_currency not in RATES or to_currency not in RATES:
        raise ValueError("Неподдерживаемая валюта")
    
    # Конвертируем через USD
    usd_amount = amount / RATES[from_currency]
    result = usd_amount * RATES[to_currency]
    
    return round(result, 2)

def get_supported_currencies():
    """Возвращает список поддерживаемых валют"""
    return list(RATES.keys())