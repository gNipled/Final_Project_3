import json
import os.path
from datetime import datetime


def load_transactions(path):
    """
    Loads information from .json file if it exists
    :param path: path to file with operations information
    :return data from .json file or none if file does not exist
    """
    if not os.path.exists(path):
        return None

    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_last_operations(data):
    """

    :param data:
    :return:
    """
    date_list = []
    last_operations = []
    for operation in data:
        if len(operation) == 7:
            continue
        if operation["state"] == "EXECUTED":
            date_list.append(operation["date"])

    date_list.sort(reverse=True)

    for date in date_list[:5]:
        for operation in data:
            if len(operation) == 7:
                continue
            if operation["date"] == date:
                last_operations.append(operation)

    return last_operations


def masking(card_number):
    """

    :param card_number:
    :return:
    """
    splited_number = card_number.split()

    if splited_number[0] == 'Счет':
        second_part = f' **{splited_number[1][-5:-1]}'
    else:
        second_part = f'{splited_number[-1][:4]} {splited_number[-1][4:6]}** **** {splited_number[-1][-5:-1]}'

    if len(splited_number) == 3:
        first_part = f'{splited_number[0]} {splited_number[1]}'
    else:
        first_part = splited_number[0]

    return(f'{first_part} {second_part}')


def format_date(date):
    """

    :param date:
    :return:
    """
    date = '2019-02-08T09:09:35.038506'
    date_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_time.strftime('%d.%m.%Y')


def print_result(last_operations):
    """

    :param data:
    :return:
    """
    for operation in last_operations:
        print(f'{format_date(operation["date"])} {operation["description"]}')
        if operation["description"] == 'Открытие вклада':
            print(f'{masking(operation["to"])}')
        else:
            print(f'{masking(operation["from"])} -> {masking(operation["to"])}')
        print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}')
