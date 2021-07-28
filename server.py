import telebot
import os
import requests
import uuid
from image import image_to_bw

token = "1916204899:AAEQs7q9ChpXFKorT6wkvhscmxVmjISIQDk"

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey")

@bot.message_handler(content_types=["text"]) 
def text(message): 
    bot.send_message(message.chat.id, 'Hello') 

@bot.message_handler(content_types=['photo'])
def photo(message):
    save_url = '/Users/User/project/banana/images/'
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    image_name = str(uuid.uuid4())+'.jpg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(save_url+image_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    path_to_bw = image_to_bw(save_url+image_name)
    img = open(path_to_bw,'rb')
    bot.send_photo(message.chat.id, img)
    os.remove(path_to_bw)

bot.polling()


