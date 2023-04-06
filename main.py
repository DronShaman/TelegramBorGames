# Done! Congratulations on your new bot. You will find it at t.me/BotoFed_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot,ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 6256786801:AAF2nxsgMCek4TjCOSNWIXe6GglsEy8ftZ0
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

from config import *  # import my token
import telebot  # import telebot with api
import requests
import time

# Задаем токен бота и ID чата, куда будут отправляться оповещения
bot = telebot.TeleBot(TELEGRAM_TOKEN)
chat_id = "YOUR_CHAT_ID"

# ответ на команду /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Бот Фед Быстрый интернет запущен")

@bot.message_handler(content_types=["text"])
def bot_msg_text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Меня не взломать, фед бессмертный")
    elif message.text.startswith("Привет") or message.text.startswith("Ку") or message.text.startswith("Салют"):
        bot.send_message(message.chat.id, "Здорово, заебал")
    else:
        bot.send_message(message.chat.id, "Не знаю такой команды")

if __name__ == '__main__':
    print("Оно живое!")
    bot.infinity_polling()
    print("Конец")

# Задаем токен бота и ID чата, куда будут отправляться оповещения
chat_id = "https://t.me/dronshaman"


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
