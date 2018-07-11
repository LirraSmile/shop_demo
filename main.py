import requests

def get_bot_updates():

    url = "https://api.telegram.org/bot600232593:AAFdYV-TtqWkShMFadOwH8x9V_pAA1HtALQ/getUpdates"

    response = requests.get(url)

    #форматируем json в словарь

    decoded = response.json()

    return decoded['result']

print(get_bot_updates())
