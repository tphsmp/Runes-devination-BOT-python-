import random
from enum import Enum
from typing import List


class Runa:
    # класс руна, name - название, position - 0 - прямое положение, 1 перевернутое, ascii - символ руны в кодировке
    # letter и second_letter - соответсвующая буква английского алфавита
    # description и description_inverted - толкование руны в прямом и перевернутом положении
    def __init__(self, name, description, descriptionInverted, position, ascii, letter, second_letter, image,
                 image_inversed, send_image):
        self.name = name
        self.description = description
        self.descriptionInverted = descriptionInverted
        if name in ('Gifu', 'Hagalaz', 'Nautiz', 'Isa', 'Jera', 'Eihwaz', 'Siegel', 'Ingwaz', 'Dagaz', 'Wyrd'):
            self.position = 0
        else:
            self.position = random.randint(0, 1)
        self.ascii = ascii
        self.letter = letter
        self.second_letter = second_letter
        self.image = image
        self.image_inversed = image_inversed
        self.send_image = send_image

    def __str__(self):
        if self.position == 0:
            return "%s %s %s %s" % (self.name, self.ascii, self.description, "прямое положение")
        if self.position == 1:
            return "%s %s %s %s" % (self.name, self.ascii, self.descriptionInverted, "перевернутое положение")


class RunesLayout:
    # выборка для одной руны
    @classmethod
    def get_one_rune(cls, runes):
        runa = random.choice(runes)
        runa.send_image = runa.image_inversed if runa.position == 1 else runa.image
        return runa

    # выборка для трех и более рун
    @classmethod
    def get_list_runes(cls, runes, count=3):
        runes_for_send: List[Runa] = []
        runes_list = runes.copy()
        for i in range(count):
            runa = random.choice(runes_list)
            runa.send_image = runa.image_inversed if runa.position == 1 else runa.image
            runes_for_send.append(runa)
            runes_list.remove(runa)
        return runes_for_send
