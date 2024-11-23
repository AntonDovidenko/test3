from telebot import TeleBot
from random import choice

bot = TeleBot('6148661170:AAEi9hHxCoZ6wQkqrZ4MAFtq2zXAmPhkH68')

items = ["камень", "ножницы", "бумага"]

@bot.message_handler(func = lambda m: m.text.lower() in items)

def game(massage):
    bot_vibor = choice(items)
    user_vibor = massage.text.lower()

    if bot_vibor == "камень"  and user_vibor == "бумага":
        msg = "Ты выйграл"
    elif bot_vibor == "бумага"  and user_vibor == "ножницы":
        msg = "Ты выйграл"
    elif bot_vibor == "ножницы"  and user_vibor == "камень": 
        msg = "Ты выйграл"
    elif bot_vibor == user_vibor: 
        msg = "Ничья"
    else:
        msg = "Ты проиграл"

    bot.send_message(massage.chat.id, bot_vibor)
    bot.send_message(massage.chat.id, msg)

bot.polling()