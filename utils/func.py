import json


def read_json():
    """
    Читает файл json.py в список
    :return: list
    """
    try:
        with open('../src/operations.json', 'r', encoding='cp65001') as file:
            file_str = file.read()
            file_lst = json.loads(file_str)
            return file_lst
    except IOError:
        print('Ошибка при чтении файла')


def trans_date(value):
    """
    Модифицирует представление даты
    :param value:
    :return:
    """
    date = str(value)
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


def check_alpha_digit(value):
    """
    Разделяет строку на название карты и номер счёта
    :param value: str
    :return: word, digit
    """
    word = ''
    digit = ''
    for i in value:
        if i.isdigit():
            digit += i
        else:
            word += i
    return word, digit
