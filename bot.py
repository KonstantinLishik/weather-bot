import ast
from bs4 import BeautifulSoup
import requests
url='https://pogoda.ngs.ru'
def weather(smth):
	a=requests.get(url, timeout=60)
	b=BeautifulSoup(a.content, 'html.parser')
	c=b.find(class_='value__main')
	d=str(c)
	s=d[27:28]
	f=d[28:29]
	g=ast.literal_eval(s)
	h=ast.literal_eval(f)
	if type(g)==int:
		if type(h)==int:
			x=d[26:29]
		else:
			x=d[26:28]
	else:
		x=d[26:27]
	return x 

	
import telebot
from telebot import types
bot=telebot.TeleBot('1355506133:AAGFQeKhm1BPu03EaSISA_nMqYNUu15ydiE')
@bot.message_handler(commands=['start'])
def start_message(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Хочу узнать погоду")
	item2 = types.KeyboardButton("Да")
	item3 = types.KeyboardButton("Нет")
	item4 = types.KeyboardButton("Как дела?")
	markup.add(item1, item2, item3, item4)
	bot.send_message(message.chat.id, 'Привет, хочешь узнать сколько сейчас градусов?', reply_markup=markup)

	
@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'Хочу узнать погоду':
		x = weather(0)
		bot.send_message(message.chat.id, x)
		bot.send_message(message.chat.id, 'Хорошая погода!')
	elif message.text == 'Да':
		bot.send_message(message.chat.id, 'Здорово!')
	elif message.text == 'Нет':
		bot.send_message(message.chat.id, 'Жаль')
	elif message.text == 'Как дела?':
		bot.send_message(message.chat.id, 'Хорошо, у тебя тоже?')
	else:
		bot.send_message(message.chat.id, 'Да или нет? Я тебя не понимаю(')
		
		
bot.polling()
