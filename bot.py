import telebot
from telebot import types
from main import encode
from main import decode

bot = telebot.TeleBot('7931938745:AAHPWGFEM_lpWRomNGKfFRmxfDyH06x94LM')

cube = [
    (
        "А", "Б", "В",
        "Г", "Д", "Е",
        "Ё", "Ж", "З",
    ),
    (
        "И", "Й", "К",
        "Л", "М", "Н",
        "О", "П", "Р",
    ),
    (
        "С", "Т", "У",
        "Ф", "Х", "Ц",
        "Ч", "Ш", "Щ",
    ),
    (
        "Ъ", "Ы", "Ь",
        "Э", "Ю", "Я",
        "1", "2", "3",
    ),
    (
        "_", ".", ",",
        "?", "!", ")",
        "(", "}", "{",
    ),
    (
        ":", "0", "9",
        "-", "8", "7",
        "4", "5", "6",
    ),
]



@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Закодировать")
    btn2 = types.KeyboardButton('Раскодировать')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выберите метод обработки")

state = None

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global state
    if message.text == "Encode":
        state = message.text
        bot.send_message(message.from_user.id, "Введите сообщение для кодирования")
    elif message.text == "Decode":
        state = message.text
        bot.send_message(message.from_user.id, "Введите сообщение для раскодирования")
    else:
        print(state)
        # hui = encode(str(message.text).replace(" ", "№").upper(), cube)
        # print(hui)
        if state == "Encode":
            hui = encode(str(message.text).replace(" ", "№").upper(), cube)
            bot.send_message(message.from_user.id, hui)
        elif state == "Decode":
            hui = decode(message.text, cube)
            bot.send_message(message.from_user.id, hui)

    

bot.polling(none_stop=True, interval=0)
