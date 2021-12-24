import const

from runa import Runa

from random import choice

import telebot

from telebot import types

bot = telebot.TeleBot(const.TOKEN)

runes = [Runa("Fehu", "sd", "id", "", "", "\u16A0"),
         Runa("Uruz", "sd", "id", "", "", "\u16A2"),
         Runa("Thurusaz", "sd", "id", "", "", "\u16A6"),
         Runa("Ansuz", "sd", "id", "", "", "\u16A8"),
         Runa("Raido", "sd", "id", "", "", "\u16B1"),
         Runa("Kenaz", "sd", "id", "", "", "\u16B2"),
         Runa("Gifu", "sd", "sd", "", "", "\u16B7"),
         Runa("Wunjo", "sd", "id", "", "", "\u16B9"),
         Runa("Hagalaz", "sd", "sd", "", "", "\u16BA"),
         Runa("Nautiz", "sd", "sd", "", "", "\u16BE"),
         Runa("Isa", "sd", "sd", "", "", "\u16C1"),
         Runa("Jera", "sd", "sd", "", "", "\u16C3"),
         Runa("Eihwaz", "sd", "sd", "", "", "\u16C7"),
         Runa("Perthro", "sd", "id", "", "", "\u16C8"),
         Runa("Algiz", "sd", "id", "", "", "\u16C9"),
         Runa("Siegel", "sd", "sd", "", "", "\u16CB"),
         Runa("Tyr", "sd", "id", "", "", "\u16CF"),
         Runa("Berkana", "sd", "id", "", "", "\u16D2"),
         Runa("Ehwaz", "sd", "id", "", "", "\u16D6"),
         Runa("Mannaz", "sd", "id", "", "", "\u16D7"),
         Runa("Laguz", "sd", "id", "", "", "\u16DA"),
         Runa("Ingwaz", "sd", "sd", "", "", "\u16DD"),
         Runa("Dagaz", "sd", "sd", "", "", "\u16DE"),
         Runa("Othel", "sd", "id", "", "", "\u16DF"),
         Runa("Wyrd", "sd", "sd", "", "", "\u25CB")]

newList = []


# Метод, который получает сообщения и обрабатывает их


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я онлайн оракул.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_runeoftheday = types.InlineKeyboardButton(text='Руна дня', callback_data='runeoftheday')
        keyboard.add(key_runeoftheday)
        key_threerunes = types.InlineKeyboardButton(text='Три руны', callback_data='threerunes')
        keyboard.add(key_threerunes)
        bot.send_message(message.from_user.id, text='Выбери расклад', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "runeoftheday":
        # msg = choice(runes)
        # Отправляем текст в Телеграм
        msg = choice(runes)
        if msg.position == 0 or msg.name == "Gifu" or msg.name == "Hagalaz" or msg.name == "Nautiz" \
                or msg.name == "Isa" or msg.name == "Jera" or msg.name == "Eihwaz" or msg.name == "Siegel" \
                or msg.name == "Ingwaz" or msg.name == "Dagaz" or msg.name == "Wyrd":
            msg.position = 0
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "threerunes":
        for i in range(3):
            msg1 = choice(runes)
            newList.append(msg1)
            runes.remove(msg1)

            bot.send_message(call.message.chat.id, msg1)


print("Bot is running")

# проверка правильности отображения символов рун
# for i in runes:
# print(i.name, i.ascii, i.position)

bot.polling(none_stop=True, interval=0)
