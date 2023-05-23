class Operations:
    def __init__(self, all_operations):
        self.all_operations = all_operations
        self.__last_operations = self.__set_last_operations()

    def __repr__(self):
        return f"Operations({self.all_operations})"

    @property
    def all_operations(self):
        return self.__all_operations

    @all_operations.setter
    def all_operations(self, value):
        if type(value) != list or type(value[0]) != dict:
            raise TypeError
        self.__all_operations = value

    def __set_last_operations(self):
        operations = filter(lambda item: item.get("date"), self.all_operations)
        operations = sorted(operations, key=lambda item: item["date"])[:-6:-1]
        return operations

    @staticmethod
    def __date_reversed(date):
        return ".".join(date.split("T")[0].split("-")[::-1])

    @staticmethod
    def __check_state(operation):
        return "ВЫПОЛНЕНО" if operation == 'EXECUTED' else 'ОТМЕНЕННО'

    @staticmethod
    def __hide_operation(order):
        if len(order) == 16:
            return order[:4] + " " + order[4:6] + "**" + " **** " + order[12:16]
        else:
            return "**" + order[len(order) - 4:]

    @staticmethod
    def __check_from_operation(operation):
        if operation.get('from') is not None:
            order_from, order_to = operation['from'].split(), operation['to'].split()
            order_from[-1], order_to[-1] = Operations.__hide_operation(order_from[-1]), \
                Operations.__hide_operation(order_to[-1])

            return " ".join(order_from) + " -> " + " ".join(order_to) + '\n'
        else:
            return

    def output_last_operations(self):
        for operation in self.__last_operations:
            print(f"Операция: {operation['id']}\n"
                  f"{self.__date_reversed(operation['date'])} {operation['description']}\n"
                  f"{self.__check_from_operation(operation)}"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
                  f"Статус: {self.__check_state(operation['state'])}\n")
