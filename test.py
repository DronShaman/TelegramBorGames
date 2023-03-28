from config import * #import token
import telebot #to work with API

#create bot instance
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#answer for command /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Привет")

#answer to messages that are not commands
@bot.message_handler(content_types=["text"])
def bot_msg_text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Команда недоступна")
    else:
         bot.send_message(message.chat.id, "Это не команда")

#MAIN PROGRAM
if name== 'main':
    print('Bot started!')
    bot.infinity_polling()
    print("End")