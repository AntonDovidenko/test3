from telebot import TeleBot, types
from time import time
from random import randint

bot = TeleBot("6148661170:AAEi9hHxCoZ6wQkqrZ4MAFtq2zXAmPhkH68")

url = 0

with open('bad_words.txt', 'r', encoding='utf-8') as f:
    data = [word.strip().lower() for word in f.readlines()]

def is_group(message):
    return message.chat.type in ('group', 'supergroup')

def has_bad_words(text):
    message_words = text.split(' ')
    for word in message_words:
        if word in data:
            return True
    return False


@bot.message_handler(func=lambda message: message.entities is not None and is_group(message))
def delate_links(message):
    global url
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            if url <= 1:
                bot.send_message(message.chat.id, text='Сообщение не отправленно. В группе запрещенно распростронение ссылок')            
                bot.delete_message(message.chat.id, message.message_id) 
                url += 1
            elif url > 1:
                bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time())
                bot.send_message(message.chat.id, text='Вы были заблокированны модератором на 2 мин, за рассылку в группе')            
                bot.delete_message(message.chat.id, message.message_id) 

@bot.message_handler(func=lambda message: has_bad_words(message.text.lower()) and is_group(message))
def bad_bad_words(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time())
    bot.send_message(message.chat.id, text='Вы были заблокированны модератором на 2 мин, за употребление запрещённой лексики в группе')
    bot.delete_message(message.chat.id, message.message_id) 

if __name__ == '__main__':
    bot.polling(non_stop=True) 
