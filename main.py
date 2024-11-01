import telebot
from telebot import types
from PIL import Image, ImageDraw, ImageFont
import math
import os

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def welcome1(message):
    global idusers
    idusers = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ")
    item2 = types.KeyboardButton("О БОТЕ")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - Помогу тебе с математикой\nЧто-бы дать мне задание нажмите на кнопки ниже".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

def welcome(message):
    def welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ")
        item2 = types.KeyboardButton("О БОТЕ")

        markup.add(item1, item2)

        bot.send_message(message.chat.id,"Что-бы дать мне задание нажмите на кнопки ниже".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_menu(message):
    if message.chat.type == 'private':
        if message.text == 'РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ':
            msg = bot.send_message(message.chat.id, "Введите коэффиценты одной строчкой: a b c")
            bot.register_next_step_handler(msg, result)

def result(message):
    coff = message.text
    coff = coff.split()
    if len(coff) == 3:
        try:
            a = int(coff[0])
            b = int(coff[1])
            c = int(coff[2])
            dis = b ** 2 - 4 * a * c
            if dis < 0:
                bot.send_message(message.chat.id, "Квадратное уравнение не имеет корней")
                welcome(message)
            elif dis == 0:
                x = -b / (2*a)
                bot.send_message(message.chat.id, f"Дискриминант равен 0 поэтому\nКорень уравнения: x ={x}")
            elif dis > 0:
                x1 = round((-b + math.sqrt(dis)) / (2 * a), 3)
                x2 = round((-b - math.sqrt(dis)) / (2 * a), 3)
                img = Image.new('RGBA', (1000,800), "gray")
                idraw = ImageDraw.Draw(img)
                headline = ImageFont.truetype('wiguru-13.ttf', size=30)

                idraw.text((40, 10), "*ТУТ ваше уравнения*", font=headline)
                idraw.text((40, 60), f"D = {b}² - 4 ({a} · {c}) = {dis}", font=headline)

                idraw.text((40, 120), f"X1 = {-b} + √{dis}", font=headline)
                idraw.line((95, 148, 290, 148), fill='white', width=3)
                idraw.text((130, 150), f"2 · {a}", font=headline)
                idraw.text((300, 134), f"=", font=headline)
                idraw.text((320, 134), f"{x1}", font=headline)

                idraw.text((40, 210), f"X2 = {-b} - √{dis}", font=headline)
                idraw.line((95, 238, 290, 238), fill='white', width=3)
                idraw.text((130, 240), f"2 · {a}", font=headline)
                idraw.text((300, 227), f"=", font=headline)
                idraw.text((320, 227), f"{x2}", font=headline)

                img.save(f'resultsuser/{idusers}.png')

                resultphoto = open(f"resultsuser/{idusers}.png", 'rb')
                bot.send_photo(message.chat.id, resultphoto)

                bot.send_message(message.chat.id, f"Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}")

                #os.remove(f"resultsuser/{idusers}.png")

                welcome(message)
        except:
            bot.send_message(message.chat.id, f"Не верно заданы коэффиценты")
            welcome(message)

    else:
        bot.send_message(message.chat.id, "Сообщение задано не в верном формате\nПопробуйте заново")
        welcome(message)

bot.infinity_polling()