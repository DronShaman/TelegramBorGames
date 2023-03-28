# Done! Congratulations on your new bot. You will find it at t.me/BotoFed_bot. You can now add a description, about section
# and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot,
# ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 6256786801:AAF2nxsgMCek4TjCOSNWIXe6GglsEy8ftZ0
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

from config import *  # import my token
import telebot  # import telebot with api

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ответна команду /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Ну и зачем ты команды запускаешь???")

if __name__ == '__main__':
    print("Оно живое!!!")
    bot.infinity_polling()
    print("Конец")

@bot.message_handler(commands=["text"])
def bot_msg_text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Команда не доступна")
    else:
        bot.send_message(message.chat.id, "Это не команда")
