import requests

def get_bot_updates(limit):

    url = "https://api.telegram.org/bot600232593:AAFdYV-TtqWkShMFadOwH8x9V_pAA1HtALQ/getUpdates"

    # записываем параметры в словарь

    par = {'limit':limit}

    # передаем словарь в аргумент функции
    
    response = requests.get(url, params=par)


    #форматируем json в словарь

    decoded = response.json()

    return decoded['result']

print(get_bot_updates(5))
