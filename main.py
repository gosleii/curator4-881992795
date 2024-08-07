import telebot

bot = telebot.TeleBot('7471538162:AAGZkQlizSJ9Re_wObVfz301kK16D-6GFjE')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '*Привет*', parse_mode='Markdown')


@bot.message_handler(commands=['Yes_or_No?'])
def YesorNo(message):
    bot.send_message(message.chat.id, '_YES_', parse_mode='Markdown')


bot.infinity_polling()