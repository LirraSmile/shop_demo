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


first_update = [result]

# получаем текст сообщения

for item in result:

    text = item['message']['text']

    #message_id = item['message']['message_id']

    update_id = item['update_id']

    new_offset = update_id + 1     

    print(update_id, text)

    get_bot_updates(5, new_offset)






