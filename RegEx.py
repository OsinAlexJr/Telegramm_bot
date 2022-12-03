# Шаблоны для нахождения нужной информации

import re


class Text:
    def __init__(self):
        self.pattern_1 = re.compile('\d{10}\s-\s\w{1,}')
        self.pattern_2 = re.compile('\d{10}-\w{1,}')
        self.pattern_3 = re.compile('\d{10}\s\w{1,}')
        self.pattern_4 = re.compile('\d{10}\s-\w{1,}')
        self.pattern_5 = re.compile('\d{10}-\s\w{1,}')

    def __call__(self, text):
        if self.pattern_1.search(text) != None:
            return (text[:10], text[13:])
        elif self.pattern_2.search(text) != None or self.pattern_3.search(text) != None:
            return (text[:10], text[11:])
        elif self.pattern_4.search(text) != None or self.pattern_5.search(text) != None:
            return (text[:10], text[12:])
        else:
            return None

class Set:
    def __init__(self):
        self.pattern_1 = re.compile('\d{1}\s-\s\w{1,}')
        self.pattern_2 = re.compile('\d{1}-\w{1,}')
        self.pattern_3 = re.compile('\d{1}\s\w{1,}')
        self.pattern_4 = re.compile('\d{1}\s-\w{1,}')
        self.pattern_5 = re.compile('\d{1}-\s\w{1,}')
    def __call__(self, text):
        if self.pattern_1.search(text) != None:
            return (text[:1], text[4:])
        elif self.pattern_2.search(text) != None or self.pattern_3.search(text) != None:
            return (text[:1], text[2:])
        elif self.pattern_4.search(text) != None or self.pattern_5.search(text) != None:
            return (text[:1], text[3:])
        else:
            return None


def Check_result(point: tuple) -> bool: # Функция, которая проверяет возвращаемый результат (строка 54)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
    if point == None:
        return True
    for symbols in point[1]:
        for symbol in numbers:
            if symbols == symbol:
                return True
        return False

