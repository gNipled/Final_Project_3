import json
import os.path


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



def get_sorted_id(data):
    """

    :param data:
    :return:
    """
    pass


def masking_card(card_number):
    """

    :param card_number:
    :return:
    """
    pass


def masking_account(account_number):
    """

    :param account_number:
    :return:
    """
    pass


def format_date(date):
    """

    :param date:
    :return:
    """
    pass


def print_result(data, id_last):
    """

    :param data:
    :return:
    """
    pass
