#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict


_NUM_STRING_RU = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот'
}


_FRACTION_STRING_RU = {
    2: 'половина',
    3: 'треть',
    4: 'четверть',
    5: 'пятая',
    6: 'шестая',
    7: 'седьмая',
    8: 'восьмая',
    9: 'девятая',
    10: 'десятая',
    11: 'одиннадцатая',
    12: 'двенадцатая',
    13: 'тринадцатая',
    14: 'четырнадцатая',
    15: 'пятнадцатая',
    16: 'шестнадцатая',
    17: 'семнадцатая',
    18: 'восемнадцатая',
    19: 'девятнадцатая',
    20: 'двадцатая',
    30: 'тридцатая',
    40: 'сороковая',
    50: 'пятидесятая',
    60: 'шестидесятая',
    70: 'семидесятая',
    80: 'восьмидесятая',
    90: 'девяностая',
    1e2: 'сотая',
    1e3: 'тысячная',
    1e6: 'миллионная',
    1e9: 'миллиардная'
}


_SHORT_SCALE_RU = OrderedDict([
    (1e3, 'тысяча'),
    (1e6, "миллион"),
    (1e9, "миллиард"),
    (1e12, "триллион"),
    (1e15, "квадриллион"),
    (1e18, "квинтиллион"),
    (1e21, "секстиллион"),
    (1e24, "септиллион"),
    (1e27, "октиллион"),
    (1e30, "нониллион"),
    (1e33, "дециллион"),
    (1e36, "ундециллион"),
    (1e39, "дуодециллион"),
    (1e42, "тредециллион"),
    (1e45, "кваттордециллион"),
    (1e48, "квиндециллион"),
    (1e51, "сексдециллион"),
    (1e54, "септендециллион"),
    (1e57, "октодециллион"),
    (1e60, "новемдециллион"),
    (1e63, "вигинтиллион"),
    (1e66, "унвигинтиллион"),
    (1e69, "дуовигинтиллион"),
    (1e72, "тревигинтиллион"),
    (1e75, "кватторвигинтиллион"),
    (1e78, "квинвигинтиллион"),
    (1e81, "секснвигинтиллион"),
    (1e84, "септенвигинтиллион"),
    (1e87, "октовигинтиллион"),
    (1e90, "новемвигинтиллион"),
    (1e93, "тригинтиллион"),
])


_LONG_SCALE_RU = OrderedDict([
    (1e3, 'тысяча'),
    (1e6, "миллион"),
    (1e9, "миллиард"),
    (1e12, "биллион"),
    (1e15, "биллиард"),
    (1e18, "триллион"),
    (1e21, "триллиард"),
    (1e24, "квадриллион"),
    (1e27, "квадриллиард"),
    (1e30, "квинтиллион"),
    (1e33, "квинтиллиард"),
    (1e36, "секстиллион"),
    (1e39, "секстиллиард"),
    (1e42, "септиллион"),
    (1e45, "септиллиард"),
    (1e48, "октиллион"),
    (1e51, "октиллиард"),
    (1e54, "нониллион"),
    (1e57, "нониллиард"),
    (1e60, "дециллион"),
    (1e63, "дециллиард"),
    (1e66, "ундециллион"),
    (1e72, "дуодециллион"),
    (1e78, "тредециллион"),
    (1e84, "кваттордециллион"),
    (1e90, "квиндециллион"),
    (1e96, "сексдециллион"),
    (1e102, "септендециллион"),
    (1e108, "октодециллион"),
    (1e114, "новемдециллион"),
    (1e120, "вигинтиллион"),
])


_ORDINAL_BASE_RU = {
    1: 'первый',
    2: 'второй',
    3: 'третий',
    4: 'четвёртый',
    5: 'пятый',
    6: 'шестой',
    7: 'седьмой',
    8: 'восьмой',
    9: 'девятый',
    10: 'десятый',
    11: 'одиннадцатый',
    12: 'двенадцатый',
    13: 'тринадцатый',
    14: 'четырнадцатый',
    15: 'пятнадцатый',
    16: 'шестнадцатый',
    17: 'семнадцатый',
    18: 'восемнадцатый',
    19: 'девятнадцатый',
    20: 'двадцатый',
    30: 'тридцатый',
    40: "сороковой",
    50: "пятидесятый",
    60: "шестидесятый",
    70: "семидесятый",
    80: "восьмидесятый",
    90: "девяностый",
    1e2: "сотый",
    2e2: "двухсотый",
    3e2: "трёхсотый",
    4e2: "четырёхсотый",
    5e2: "пятисотый",
    6e2: "шестисотый",
    7e2: "семисотый",
    8e2: "восьмисотый",
    9e2: "девятисотый",
    1e3: "тысячный"
}


_SHORT_ORDINAL_RU = {
    1e6: "миллион",
    1e9: "миллиард",
    1e12: "триллион",
    1e15: "квадриллион",
    1e18: "квинтиллион",
    1e21: "секстиллион",
    1e24: "септиллион",
    1e27: "октиллион",
    1e30: "нониллион",
    1e33: "дециллион",
    1e36: "ундециллион",
    1e39: "дуодециллион",
    1e42: "тредециллион",
    1e45: "кваттордециллион",
    1e48: "квиндециллион",
    1e51: "сексдециллион",
    1e54: "септендециллион",
    1e57: "октодециллион",
    1e60: "новемдециллион",
    1e63: "вигинтиллион"
}
_SHORT_ORDINAL_RU.update(_ORDINAL_BASE_RU)


_LONG_ORDINAL_RU = {
    1e6: "миллион",
    1e9: "миллиард",
    1e12: "биллион",
    1e15: "биллиард",
    1e18: "триллион",
    1e21: "триллиард",
    1e24: "квадриллион",
    1e27: "квадриллиард",
    1e30: "квинтиллион",
    1e33: "квинтиллиард",
    1e36: "секстиллион",
    1e39: "секстиллиард",
    1e42: "септиллион",
    1e45: "септиллиард",
    1e48: "октиллион",
    1e51: "октиллиард",
    1e54: "нониллион",
    1e57: "нониллиард",
    1e60: "дециллион",
    1e63: "дециллиард",
    1e66: "ундециллион",
    1e72: "дуодециллион",
    1e78: "тредециллион",
    1e84: "кваттордециллион",
    1e90: "квиндециллион",
    1e96: "сексдециллион",
    1e102: "септендециллион",
    1e108: "октодециллион",
    1e114: "новемдециллион",
    1e120: "вигинтиллион"
}
_LONG_ORDINAL_RU.update(_ORDINAL_BASE_RU)

# Months

_MONTHS_CONVERSION = {
    0: "january",
    1: "february",
    2: "march",
    3: "april",
    4: "may",
    5: "june",
    6: "july",
    7: "august",
    8: "september",
    9: "october",
    10: "november",
    11: "december"
}

_MONTHS_RU = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
             'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
             'декабрь']

# Time
_TIME_UNITS_CONVERSION = {
    'микросекунд': 'microseconds',
    'милисекунд': 'milliseconds',
    'секунда': 'seconds',
    'секунды': 'seconds',
    'секунд': 'seconds',
    'минута': 'minutes',
    'минуты': 'minutes',
    'минут': 'minutes',
    'час': 'hours',
    'часа': 'hours',
    'часов': 'hours',
    'день': 'days',
    'дня': 'days',
    'дней': 'days',
    'неделя': 'weeks',
    'недели': 'weeks',
    'недель': 'weeks'
}