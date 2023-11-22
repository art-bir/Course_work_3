from utils import *


def main():
    """Функция вывода последних пяти EXECUTED транзакций"""

    # Количество транзакций
    transactions_number = 5

    tran_list = read_json()
    for i in range(transactions_number):
        tran_dict = tran_list[i]

        # Проверяет EXECUTED
        if tran_dict['state'] == 'EXECUTED':
            to_account = trans_card_account(tran_dict['to'], 'to')
            date = trans_date(tran_dict['date'])

            # Проверяет наличие from в словаре
            if list(tran_dict)[5] == 'from':
                from_account = trans_card_account(tran_dict['from'], 'from')
                print(f"""
                     {date} {tran_dict['description']}
                     {from_account} -> {to_account}
                     {tran_dict['operationAmount']['amount']} {tran_dict['operationAmount']['currency']['name']}
                 """)
            else:
                print(f"""
                      {date} {tran_dict['description']}
                       -> {to_account}
                      {tran_dict['operationAmount']['amount']} {tran_dict['operationAmount']['currency']['name']}
                  """)


if __name__ == '__main__':
    main()
