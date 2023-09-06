from utils import utils
import config

operations = [{
    "id": 917824439,
    "state": "EXECUTED",
    "date": "2019-07-18T12:27:13.355343",
    "operationAmount": {
        "amount": "82139.20",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Platinum 6942697754917688",
    "to": "МИР 2956603572573342"
},
    {
        "id": 121646999,
        "state": "CANCELED",
        "date": "2018-06-08T16:14:59.936274",
        "operationAmount": {
            "amount": "91121.62",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7552745726849311",
        "to": "Счет 34799481846914116850"
    }, {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    }, {}]

test_result_1 = ('18.07.2019 Перевод с карты на карту\n'
                 'Visa Platinum 6942 69** **** 7688 -> МИР 2956 60** **** 3342\n82139.20 руб.')
test_result_2 = '15.07.2019 Открытие вклада\nСчет **2265\n92688.46 USD'


def test_load_transaction():
    assert not utils.load_transactions('asdasd.scz')
    assert type(utils.load_transactions(config.PATH)) == list


def test_get_last_operations():
    assert not utils.get_last_operations('')
    assert len(utils.get_last_operations([])) == 0
    assert len(utils.get_last_operations([operations[1]])) == 0
    assert len(utils.get_last_operations(operations)) == 2
    assert utils.get_last_operations(operations)[0] == operations[0]


def test_masking():
    assert utils.masking(operations[2]["to"]) == "Счет **2265"
    assert utils.masking(operations[0]["from"]) == "Visa Platinum 6942 69** **** 7688"


def test_format_date():
    assert utils.format_date(operations[1]["date"]) == '08.06.2018'


def test_print_result():
    assert utils.print_result(operations[0]) == test_result_1
    assert utils.print_result(operations[2]) == test_result_2
