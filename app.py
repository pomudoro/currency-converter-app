"""
Flask веб-приложение для конвертера валют
"""
from flask import Flask, render_template, request, jsonify
import sys
import os

# Добавляем src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from converter import convert_currency, get_supported_currencies

app = Flask(__name__)

@app.route('/')
def index():
    """Главная страница"""
    currencies = get_supported_currencies()
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    """API для конвертации валют"""
    try:
        data = request.get_json()
        amount = float(data['amount'])
        from_currency = data['from_currency']
        to_currency = data['to_currency']
        
        result = convert_currency(amount, from_currency, to_currency)
        
        return jsonify({
            'success': True,
            'result': result,
            'message': f'{amount} {from_currency} = {result} {to_currency}'
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Ошибка конвертации'
        }), 500

@app.route('/test')
def test():
    """Тестовая страница без шаблона"""
    return '''
    <h1>🚀 Flask работает!</h1>
    <p>Если видишь это — сервер запущен корректно</p>
    <p><a href="/">← Вернуться на главную</a></p>
    '''

if __name__ == '__main__':
    # Получаем порт из переменной окружения (для Railway)
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # В продакшене отключаем debug
    debug_mode = os.environ.get('ENVIRONMENT') != 'production'
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)