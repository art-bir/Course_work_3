import datetime
import json


def read_json(file):
    """
    Читает файл json.py и возвращает список словарей
    :return: list
    """
    try:
        with open(file, 'r', encoding='cp65001') as file:
            file_str = file.read()
            file_lst = json.loads(file_str)
            return file_lst
    except IOError:
        print("Ошибка при чтении файла")


def trans_date(value):
    """
    Модифицирует представление даты
    :param value:
    :return:
    """
    date = str(value)
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


def split_name_and_number(value):
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


def masks_number(value, mod='to'):
    """
    Маскирует номер карты или счета в зависимости от выбора from или to
    :param value: str
    :param mod: Модификатор направления транзакции from или to
    :return: str
    """
    word, digit = split_name_and_number(value)
    if mod == 'to':
        word, digit = split_name_and_number(value)
        return f"{word} **{digit[-4:]}"
    elif mod == 'from':
        return f"{word}{digit[0:4]} {digit[5:7]}** **** {digit[-4:]}"


def change_string_to_date(dic: dict, format_date='%Y-%m-%dT%X'):
    """
    Приводит строку с датой к формату даты
    :param dic: dict
    :param format_date: ...
    :return:
    """
    date = dic.get('date')
    date = date[0:-7]
    return datetime.datetime.strptime(date, format_date)


def sort_list_by_date(data: list, reverse=True) -> list:
    """
    Сортирует список по убыванию даты и времени транзакции исключая пустые словари
    :return: ...
    """
    clear_list = []
    for i in data:
        if i.get('date'):
            clear_list.append(i)

    return sorted(clear_list, key=change_string_to_date, reverse=reverse)


def get_executed_transaction_list(lst: list) -> list:
    """
    Создаёт новый EXECUTED список
    :return:
    """
    new_list = []
    for dic in lst:
        if dic['state'] == 'EXECUTED':
            new_list.append(dic)
    return new_list
