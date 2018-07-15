import requests

from config import token

url = "https://api.telegram.org/bot"

def get_bot_updates(limit, offset):

    req = url + token + '/getUpdates'

    # записываем параметры в словарь

    par = {'limit':limit, 'offset':offset}

    # передаем словарь в аргумент функции
    
    result = requests.get(req, params=par)


    #форматируем json в словарь

    decoded = result.json()

    return decoded['result']

#print(get_bot_updates(5))

result = get_bot_updates(5, 0)


first_update = [result]

# получаем текст сообщения

for item in result:

    text = item['message']['text']

    update_id = item['update_id']

    new_offset = update_id + 1     

    print(update_id, text)

    get_bot_updates(5, new_offset)






