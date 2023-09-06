from utils import utils
import config

data = utils.load_transactions(config.PATH)
last_operations = utils.get_last_operations(data)
if not last_operations:
    print("Операций со счетами не производилось")
    quit()
for operation in last_operations:
    print(utils.print_result(operation))
