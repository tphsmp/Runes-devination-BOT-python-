import random


class Runa:
    # класс руна, name - название, position - 0 - прямое положение, 1 перевернутое, ascii - символ руны в кодировке
    # letter и second_letter - соответсвующая буква английского алфавита
    # description и description_inverted - толкование руны в прямом и перевернутом положении
    def __init__(self, name, description, descriptionInverted, position, ascii, letter, second_letter, image,
                 image_inversed):
        self.name = name
        self.description = description
        self.descriptionInverted = descriptionInverted
        # для рун не имеющих перевернутого значения по умолчанию задается всегда прямое положение
        if name in ('Gifu', 'Hagalaz', 'Nautiz', 'Isa', 'Jera', 'Eihwaz', 'Siegel', 'Ingwaz', 'Dagaz', 'Wyrd'):
            self.position = 0
        # для остальных рун положение генерируется случайно     
        else:
            self.position = random.randint(0, 1)
        self.ascii = ascii
        self.letter = letter
        self.second_letter = second_letter
        self.image = image
        self.image_inversed = image_inversed

    def __str__(self):
        if self.position == 0:
            return "%s %s %s %s" % (self.name, self.ascii, self.description, "прямое положение")
        if self.position == 1:
            return "%s %s %s %s" % (self.name, self.ascii, self.descriptionInverted, "перевернутое положение")


class RunesLayout:
    @classmethod
    async def get_rune(cls, runa, message=None):
        from aiogram_main import bot
        from lists import runes
        runes1 = runes.copy()
        if runa.position == 0:
            with open(runa.image, 'rb') as runa_image:
                await bot.send_photo(message, photo=runa_image, disable_notification=True)
        if runa.position == 1:
            with open(runa.image_inversed, 'rb') as runa_image:
                await bot.send_photo(message, photo=runa_image, disable_notification=True)
        runa1 = str(runa)
        runes1.remove(runa)
        await bot.send_message(message, runa1)
