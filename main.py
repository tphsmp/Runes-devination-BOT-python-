from aiogram import Bot, Dispatcher, executor, types

from lists import runes
from config import TOKEN
from runa import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# обработка команды /start при отправке команды бот выводит две кнопки для выбора рунного расклада
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message['from']['last_name']}! Я рунический оракул и могу "
                                                 f"помочь тебе советом рун. Просто выбери действие:\n\n"
                                                 f"/one_rune - Руна дня. Даст тебе совет на сегодняшний день.\n\n"
                                                 f"/three_runes - Расклад из трех рун. Поможет тебе разобраться в ситуации.\n\n"
                                                 f"Если хочешь знать как твое имя пишется рунами - напиши мне свое имя латинскими буквами")


# обработка команд расклада
@dp.message_handler(commands=['one_rune'])
async def one_rune_command(message):
    runa = RunesLayout.get_one_rune(runes)
    await bot_actions(message, runa)


@dp.message_handler(commands=['three_runes'])
async def three_runes_command(message):
    list_runes = RunesLayout.get_list_runes(runes)
    for runa in list_runes:
        await bot_actions(message, runa)


async def bot_actions(message, runa):
    with open(runa.send_image, 'rb') as runa_image:
        await bot.send_photo(message.chat.id, photo=runa_image, disable_notification=True)
    runa1 = str(runa)
    await bot.send_message(message.chat.id, runa1)


# при отправке боту текстового сообщения он конвертирует символы латиницы в символы рун
@dp.message_handler(content_types=['text'])
async def chat_message_handle(message):
    word = str(message.text)
    word = word.upper()
    letters = []
    for letter in word:
        letters.append(letter)
    runes_for_name = {}
    for i in runes:
        runes_for_name[i.letter] = i.ascii
        if i.second_letter != "":
            runes_for_name[i.second_letter] = i.ascii
    runic_name = []
    for i in letters:
        runic_name.append(runes_for_name.get(i))
    name = "".join(runic_name)
    await bot.send_message(message.chat.id, name)


# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)