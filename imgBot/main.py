from telebot import TeleBot
import requests

bot = TeleBot('6148661170:AAEi9hHxCoZ6wQkqrZ4MAFtq2zXAmPhkH68')

def duck_img():
    url = "https://random-d.uk/api/random"
    zapros = requests.get(url)
    data = zapros.json()
    print(data)
    return data["url"]

def fox_img():
    url = "https://randomfox.ca/floof/"
    zapros = requests.get(url)
    data = zapros.json()
    print(data)
    return data["image"]

@bot.message_handler(commands=["duck"]) 
def duck(massege):
    img = duck_img()
    bot.send_message(massege.chat.id, img)

@bot.message_handler(commands=["fox"]) 
def fox(massege):
    img = fox_img()
    bot.send_message(massege.chat.id, img)


bot.polling()