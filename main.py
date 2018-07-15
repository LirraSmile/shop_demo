import requests

from config import token

url = "https://api.telegram.org/bot"

url_crypto = "https://api.cryptonator.com/api/ticker"

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

def get_currencies(bace):

    request = url_crypto + bace + '-usd'

    params = {'bace': bace}

    response = requests.get(request, params = params)

    decoded = result.json()

    for item in decoded:

        price = item['ticker']['price']

    return price

# Отвечаем на сообщения

def sent_message(chat, text):

    request = url + token + '/sendMessage'

    params = {'chat_id': chat, 'text': text}

    response = requests.post(request, params = params)

    return response



def get_command(text):



    if text == '/start':

        sent_message(id_sender, 'Hello, can I help u?')

    elif text == '/btc':

        bace = 'BTC'

        sent_message(id_sender, get_currencies(bace))

    elif text == '/eth':

        bace = 'ETH'

        sent_message(id_sender, get_currencies(bace))

    else:

        sent_message(id_sender, 'Do not understand u. Please, try again')


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








