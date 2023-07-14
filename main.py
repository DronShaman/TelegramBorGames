# Done! Congratulations on your new bot. You will find it at t.me/BotoFed_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot,ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
# Use this token to access the HTTP API:
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

from config import *  # import my token
import telebot  # import telebot with api

# Получаем токен от чат бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

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