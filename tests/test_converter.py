"""
Тесты для конвертера валют
"""
import pytest
import sys
import os

# Добавляем src в путь для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from converter import convert_currency, get_supported_currencies

class TestCurrencyConverter:
    """Тесты конвертера валют"""
    
    def test_usd_to_eur(self):
        """Тест конвертации USD -> EUR"""
        result = convert_currency(100, 'USD', 'EUR')
        assert result == 85.0
    
    def test_eur_to_usd(self):
        """Тест конвертации EUR -> USD"""
        result = convert_currency(85, 'EUR', 'USD')
        assert result == 100.0
    
    def test_same_currency(self):
        """Тест конвертации в ту же валюту"""
        result = convert_currency(100, 'USD', 'USD')
        assert result == 100.0
    
    def test_rub_to_gbp(self):
        """Тест конвертации RUB -> GBP"""
        result = convert_currency(75, 'RUB', 'GBP')
        assert result == 0.73
    
    def test_invalid_currency(self):
        """Тест с неподдерживаемой валютой"""
        with pytest.raises(ValueError):
            convert_currency(100, 'USD', 'JPY')
    
    def test_zero_amount(self):
        """Тест с нулевой суммой"""
        result = convert_currency(0, 'USD', 'EUR')
        assert result == 0.0
    
    def test_get_supported_currencies(self):
        """Тест получения списка валют"""
        currencies = get_supported_currencies()
        assert 'USD' in currencies
        assert 'EUR' in currencies
        assert 'RUB' in currencies
        assert 'GBP' in currencies
        assert len(currencies) == 4