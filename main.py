import telebot

bot = telebot.TeleBot('7317119146:AAEWOiWAs-mbH7a1cNPpzCHtMkcz1qmGs7g')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '*Привет*', parse_mode='Markdown')


@bot.message_handler(commands=['Yes_or_No?'])
def YesorNo(message):
    bot.send_message(message.chat.id, '_YES_', parse_mode='Markdown')


bot.infinity_polling()