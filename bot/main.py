import requests

from config import token

url = "https://api.telegram.org/bot"
url_crypto = "https://api.cryptonator.com/api/ticker/"

# Получаем последнее обновление
def get_bot_updates(limit, offset):
    request = url + token + '/getUpdates'
    # записываем параметры в словарь
    params = {'limit':limit, 'offset':offset}
    # передаем словарь в аргумент функции    
    result = requests.get(request, params=params)
    #форматируем json в словарь
    decoded = result.json()
    return decoded['result']

# Получаем курс криптовалюты
def get_currencies(base):
    request = url_crypto + base + '-usd'
    params = {'base': base}
    result = requests.get(request, params = params)
    decoded = result.json()
    price = decoded['ticker']['price']
    return price

# Отвечаем на сообщения

def send_message(chat, text):
    request = url + token + '/sendMessage'
    params = {'chat_id': chat, 'text': text}
    response = requests.post(request, params = params)
    return response



def get_command(text):
    if text == '/start':
        rate_text = 'Hello, can I help u?'

    elif text == '/btc':
        base = 'BTC'
        rate_text = 'Курс биткоин на сегодня 1 btc = {}'.format(get_currencies(base)) + '$'

    elif text == '/eth':
        base = 'ETH'
        rate_text = 'Курс эфира на сегодня 1 eth = {}'.format(get_currencies(base)) + '$'

    else:
        rate_text = 'Do not understand u. Please, try again'

    send_message(id_sender, rate_text)

result = get_bot_updates(5, 0)

# получаем текст сообщения
for item in result:
    text = item['message']['text']
    id_sender = item['message']['chat']['id']
    update_id = item['update_id']
    new_offset = update_id + 1 
    print(update_id, id_sender, text)
    get_bot_updates(5, new_offset) 
    get_command(text) 








