import requests

def get_bot_updates(limit, offset):

    url = "https://api.telegram.org/bot600232593:AAFdYV-TtqWkShMFadOwH8x9V_pAA1HtALQ/getUpdates"

    # записываем параметры в словарь

    par = {'limit':limit, 'offset':offset}

    # передаем словарь в аргумент функции
    
    result = requests.get(url, params=par)


    #форматируем json в словарь

    decoded = result.json()

    return decoded['result']

#print(get_bot_updates(5))

result = get_bot_updates(5, 0)

# получаем текст сообщения

first_update = result[0]

text = result[0]['message']['text']

message_id = result[0]['message']['message_id']


new_offset = message_id + 1 

# выводим текст сообщения и отмечаем прочитанным

print(message_id, text)

get_bot_updates(5, new_offset)