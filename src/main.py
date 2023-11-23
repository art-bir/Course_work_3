from utils import *


def main():
    """Функция вывода последних пяти EXECUTED транзакций"""

    # Количество транзакций
    transactions_number = 5

    json_list = read_json('../src/operations.json')

    sorted_list_by_date = sort_list_by_date(json_list)

    transactions_list = get_executed_transaction_list(sorted_list_by_date)

    for i in range(transactions_number):
        one_transaction_dic = transactions_list[i]

        # Проверяет EXECUTED
        if one_transaction_dic['state'] == 'EXECUTED':
            to_account = masks_number(one_transaction_dic['to'], 'to')
            date = trans_date(one_transaction_dic['date'])

            key_from = 5
            if list(one_transaction_dic)[key_from] == 'from':
                from_account = masks_number(one_transaction_dic['from'], 'from')
                print(f"""
                     {date} {one_transaction_dic['description']}
                     {from_account} -> {to_account}
                     {one_transaction_dic['operationAmount']['amount']} {one_transaction_dic['operationAmount']['currency']['name']}
                 """)
            else:
                print(f"""
                      {date} {one_transaction_dic['description']}
                       -> {to_account}
                      {one_transaction_dic['operationAmount']['amount']} {one_transaction_dic['operationAmount']['currency']['name']}
                  """)


if __name__ == '__main__':
    main()
