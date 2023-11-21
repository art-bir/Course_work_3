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




def print_transactions(transactions_number):
    """
    Возвращает строку N последних выполненнынх (EXECUTED) транзакций
    :param transactions_number: количество транзакций
    :return:
    """
    tran_list = read_json()
    for i in range(transactions_number):
        tran_dict = tran_list[i]

        if tran_dict['state'] == 'EXECUTED':

            try:
                from_account = trans_card_account(tran_dict['from'], 'from')
                to_account = trans_card_account(tran_dict['to'], 'to')
                date = trans_date(tran_dict['date'])
            except KeyError:
                print(f"""
                {date} {tran_dict['description']}
                 -> {to_account}
                {tran_dict['operationAmount']['amount']} {tran_dict['operationAmount']['currency']['name']}
            """)
            finally:
                print(f"""
                {date} {tran_dict['description']}
                {from_account} -> {to_account}
                {tran_dict['operationAmount']['amount']} {tran_dict['operationAmount']['currency']['name']}
            """)
