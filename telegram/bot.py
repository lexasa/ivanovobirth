import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1 вопрос")
    item2 = types.KeyboardButton("2 вопрос")
    item3 = types.KeyboardButton("3 вопрос")
    item4 = types.KeyboardButton("4 вопрос")
    item5 = types.KeyboardButton("5 вопрос")
    item6 = types.KeyboardButton("6 вопрос")
    item7 = types.KeyboardButton("7 вопрос")
    item8 = types.KeyboardButton("8 вопрос")
    item9 = types.KeyboardButton("9 вопрос")
    item10 = types.KeyboardButton("10 вопрос")
 
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - бот, созданный для проверки знаний после прочтения информации на сайте. Выбирай номер вопроса на клавиатуре. Удачи!".format(message.from_user, bot.get_me()), 
    parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "1 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Иваново', callback_data='ivanovo')
        item2 = types.InlineKeyboardButton('Ростов Великий', callback_data='rostov')
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, "Cамый старый город Золотого кольца России?", reply_markup=markup)
    elif message.text == "2 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Иваново-Вознесенск', callback_data='vosnes')
        item2 = types.InlineKeyboardButton('Иваново', callback_data='neznay')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Какое название было у города в 1871 году?", reply_markup=markup)
    elif message.text == "3 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Ивановская', callback_data='van')
        item2 = types.InlineKeyboardButton('Калининградская', callback_data='kalinin')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Одна из старейших филармоний России?", reply_markup=markup)  
    elif message.text == "4 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('кинофестиваль "зеркало"', callback_data='zerkalo')
        item2 = types.InlineKeyboardButton('фестиваль "Звезда"', callback_data='nenay')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Какое мероприятие проходит в Иваново каждый год?", reply_markup=markup) 
    elif message.text == "5 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Степанова', callback_data='step')
        item2 = types.InlineKeyboardButton('генерала Потапова', callback_data='hah')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Какой парк был назван в честь погибшего в 1920 году члена Совета рабочих и солдатских депутатов?", reply_markup=markup) 
    elif message.text == "6 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('36 гектар', callback_data='fal')
        item2 = types.InlineKeyboardButton('213 гектар', callback_data='yes')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Площадь парка культуры и отдыха имени Революции 1905 года?", reply_markup=markup) 
    elif message.text == "7 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('театральным и соковским', callback_data='teatr')
        item2 = types.InlineKeyboardButton('музыкальным и соковским', callback_data='tyl')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Какими двумя мостами ограничена набережная?", reply_markup=markup) 
    elif message.text == "8 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('"FedEx"', callback_data='aga')
        item2 = types.InlineKeyboardButton('"РИАТ"', callback_data='riat')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Какой группе компаний принадлежит музей советского автопрома?", reply_markup=markup) 
    elif message.text == "9 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Д.Ф.Фридман', callback_data='frid')
        item2 = types.InlineKeyboardButton('А.И.Панов', callback_data='pan')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "Кто был архитектором дома-корабля?", reply_markup=markup) 
    elif message.text == "10 вопрос":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('модернизм', callback_data='mod')
        item2 = types.InlineKeyboardButton('модерн', callback_data='fuck')
        markup.add(item1, item2) 
        bot.send_message(message.from_user.id, "В каком стиле выполнена Усадьба Дюрингера?", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Я не знаю, что ответить.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "rostov": #1
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "ivanovo": 
            bot.send_message(call.message.chat.id, "Иваново - самый молодой город Золотого кольца, будь внимательней!")
    if call.data == "vosnes": #2
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "neznay": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "van": #3
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "kalinin": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "zerkalo": #4
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "nenay": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "step": #5
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "hah": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "yes": #6
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "fal": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "teatr": #7
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "tyl": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "riat": #8
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "aga": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "frid": #9
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "pan": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    if call.data == "fuck": #10
        bot.send_message(call.message.chat.id, "Правильный ответ!");
    elif call.data == "mod": 
            bot.send_message(call.message.chat.id, "Неправильный ответ!")
    

bot.polling(none_stop=True, interval=0)