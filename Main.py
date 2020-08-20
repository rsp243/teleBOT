import telebot

from telebot import types

bot = telebot.TeleBot('1258857280:AAGR8kKH4M7xRPPYTBCFu7EuTcAaGh1e6Oo')

obr = bool()
obr = False


@bot.message_handler(commands=['start'])

def welcome(message): 
	keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	item1 = types.KeyboardButton('Да')
	item2 = types.KeyboardButton('Нет')
	keyboard1.add(item1, item2)

	bot.send_message(message.chat.id, "{0.first_name}, добрый день! Меня зовут <strong>{1.first_name}</strong>.\
	 Я здесь, для того чтобы помогать в решении\
	  возникающих вопросов".format(message.from_user, bot.get_me()),parse_mode='html')
	
	bot.send_message(message.chat.id, "Можно ли к Вам обращаться на ты?", reply_markup = keyboard1)
	
@bot.message_handler(content_types=['text'])

def answer1(message):
	if message.chat.type == 'private':

		keyboard1 = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton('Оформить пропуск', callback_data='make a pass')
		item2 = types.InlineKeyboardButton('Уже оформил, дальше', callback_data='lets go further')
		keyboard1.add(item1, item2)
					
		if message.text == 'Да':
			bot.send_message(message.chat.id, "Хорошо")
			obr = False			
			bot.send_message(message.chat.id, "Рад приветствовать тебя в нашей команде! Формальные вопросы с документами закончены, теперь нужно оформить тебе пропуск на территорию аэропорта", reply_markup=keyboard1)
		elif message.text == 'Нет':
			obr = True
			bot.send_message(message.chat.id, "Хорошо")			
			bot.send_message(message.chat.id, "Рад приветствовать Вас в нашей команде! Формальные вопросы с документами закончены, теперь нужно оформить Вам пропуск на территорию аэропорта", reply_markup=keyboard1)
		else:
			bot.send_message(message.chat.id, "Я не знаю, что ответить. Выберите пожалуйста варианты из кнопок, кликнув на них левой клавишей кнопки мыши")
	
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
	try:
		if call.message:
			if call.data == 'make a pass':
				bot.send_message(call.message.chat.id, "Хорошо, перейдем к оформлению твоего пропуска")
				bot.send_message(call.message.chat.id, "Необходимо перейти по этой ссылке, чтобы получить больше информации по этому вопросу <a>https://www.svo.aero/ru/partners/passes</a>", parse_mode = 'html')
			elif call.data == 'lets go further':
				bot.send_message(call.message.chat.id, "СУПЕР!")
				if obr == False:
					bot.send_message(call.message.chat.id, "У Вас есть какие-либо вопросы по вашей адаптации?")
				elif obr == True:
					bot.send_message(call.message.chat.id, "У тебя есть какие-либо вопросы по твоей адаптации?")
	except Exception as ex:
	   	print(repr(ex))

bot.polling(none_stop = True)