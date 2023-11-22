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


def trans_card_account(value, mod='to'):
    """
    Маскирует номер карты или счета в зависимости от выбора from или to
    :param value: str
    :param mod: Модификатор направления транзакции from или to
    :return: str
    """
    word, digit = check_alpha_digit(value)
    if mod == 'to':
        word, digit = check_alpha_digit(value)
        return f"{word} **{digit[-4:]}"
    elif mod == 'from':
        return f"{word}{digit[0:4]} {digit[5:7]}** **** {digit[-4:]}"





