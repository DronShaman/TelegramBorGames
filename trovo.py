import requests
import time

from main import bot

# Задаем токен бота и ID чата, куда будут отправляться оповещения
chat_id = "https://t.me/+-HjJ_LXkYBljMzMy"

# Задаем URL для получения информации о стриме на Trovo
stream_url = "https://trovo.live/s/DronShaman"

# Задаем интервал между проверками начала трансляции в секундах
check_interval = 60

# Основной цикл проверки начала трансляции
while True:
    # Отправляем GET запрос к API Trovo для получения информации о стриме
    response = requests.get(stream_url)
    data = response.json()

    # Проверяем, началась ли трансляция
    if data["streamInfo"]["streamStatus"] == "Live":
        # Если трансляция началась, отправляем сообщение в Telegram
        message = "Началась трансляция на Trovo!"
        url = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    # Ждем заданное количество секунд перед следующей проверкой
    time.sleep(check_interval)
