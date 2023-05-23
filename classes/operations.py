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
