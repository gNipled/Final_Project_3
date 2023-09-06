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
        return False

    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_last_operations(data):
    """
    Returns last 5 executed operations from data set in .json format, ignores empty data sets.
    If data set isn`t list returns False
    :param data: data set in .json format
    :return last_operations: list of last 5 operations sorted by data
    """
    if not type(data) == list:
        return False

    date_list = []
    last_operations = []

    for operation in data:
        if len(operation) == 0:
            continue
        if operation["state"] == "EXECUTED":
            date_list.append(operation["date"])

    date_list.sort(reverse=True)

    for date in date_list[:5]:
        for operation in data:
            if len(operation) == 0:
                continue
            if operation["date"] == date:
                last_operations.append(operation)

    return last_operations


def masking(card_number):
    """
    Masking card number in format "card name first 6 digits ** **** last 4 digits" or
    masking account number in format "Account **last 4 digits"
    :param card_number: Name and number of card or account in format "Name card_number(16 digits no spaces)"
    or "Name account_number(no spaces)"
    :return: string with masked card or account number
    """
    splited_number = card_number.split()

    if splited_number[0] == 'Счет':
        second_part = f'**{splited_number[1][-4:]}'
    else:
        second_part = f'{splited_number[-1][:4]} {splited_number[-1][4:6]}** **** {splited_number[-1][-4:]}'

    if len(splited_number) == 3:
        first_part = f'{splited_number[0]} {splited_number[1]}'
    else:
        first_part = splited_number[0]

    return f'{first_part} {second_part}'


def format_date(date):
    """
    Formats date as "DD.MM.YYYY"
    :param date: date in format "YYYY-MM-DD T HH:mm:ss.ms"
    :return: String with date in format "DD.MM.YYYY"
    """
    date_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_time.strftime('%d.%m.%Y')


def print_result(operation):
    """
    Formats an output massage as
    "14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб."
    In case of deposit opening formats output massage as
    "14.10.2018 Открытие вклада
    Счет **9638
    82771.72 руб."
    :param operation: information about operation in project format
    :return: string in requested format
    """
    output = ''
    output += f'{format_date(operation["date"])} {operation["description"]}\n'
    if operation["description"] == 'Открытие вклада':
        output += f'{masking(operation["to"])}\n'
    else:
        output += f'{masking(operation["from"])} -> {masking(operation["to"])}\n'
    output += f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}'
    return output
