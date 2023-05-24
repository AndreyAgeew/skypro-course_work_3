from typing import Any


class Operations:
    """
    Базовый классс Operations - предоставляет информацию о 5 последних банковских операциях
        Args:
            all_operations (list[dict]) - передает все банковские операции
        Attributes:
            self.__last_operations (list[dict]) - получает 5 последних банковский операций

    """

    def __init__(self, all_operations: list[dict]) -> None:
        """Инициализирует Operations объект со списком всех операций"""
        self.all_operations: list[dict] = all_operations
        self.__last_operations: list[dict] = self.__set_last_operations()

    def __repr__(self) -> str:
        """Возращает строковое представление объекта Operations"""
        return f"Operations({self.all_operations})"

    @property
    def all_operations(self) -> list[dict]:
        """Cвойство, которое возвращает список всех операций"""
        return self.__all_operations

    @all_operations.setter
    def all_operations(self, value: list[dict]) -> None:
        """
        Свойство-сеттер, устанавливает все операции
        :param value:  список всех операций
        :raise: TypeError: Если значение не является списком или первый элемент списка не является словарем
        """
        if type(value) != list or type(value[0]) != dict:
            raise TypeError
        self.__all_operations = value

    def __set_last_operations(self) -> list[dict]:
        """Возвращает последние 5 операций, отсортированных по дате в обратном порядке"""
        operations = filter(lambda item: item.get("date"), self.all_operations)
        operations = sorted(operations, key=lambda item: item["date"])[:-6:-1]
        return operations

    @staticmethod
    def __date_reversed(date: str) -> str:
        """Возвращает строку даты из формата «ГГГГ-ММ-ДД» в «ДД.ММ.ГГГГ»"""
        return ".".join(date.split("T")[0].split("-")[::-1])

    @staticmethod
    def __check_state(operation: str) -> str:
        """
        Проверяет состояние операции и возвращает соответствующий статуc
        :param operation: - cостояние операции
        :return: Статус операции ("ВЫПОЛНЕНО" или "ОТМЕНЕННО")
        """
        return "ВЫПОЛНЕНО" if operation == 'EXECUTED' else 'ОТМЕНЕННО'

    @staticmethod
    def __hide_operation(order: str) -> str:
        """
        Скрывает часть данных о заказе операции
        :param order:  Идентификатор заказа операции
        :return: Скрытая версия идентификатора заказа
        """
        if len(order) == 16:
            return order[:4] + " " + order[4:6] + "**" + " **** " + order[12:16]
        else:
            return "**" + order[len(order) - 4:]

    @staticmethod
    def __check_from_operation(operation: dict) -> Any:
        """
        Проверяет наличие информации об отправителе операции и скрывает часть данных
        :param operation:
        :return: Строка с информацией об отправителе и получателе операции (если есть отправитель)
        """
        if operation.get('from') is not None:
            order_from, order_to = operation['from'].split(), operation['to'].split()
            order_from[-1], order_to[-1] = Operations.__hide_operation(order_from[-1]), \
                Operations.__hide_operation(order_to[-1])

            return " ".join(order_from) + " -> " + " ".join(order_to) + '\n'
        else:
            return

    def output_last_operations(self):
        """Выводит информацию о последних операциях"""
        for operation in self.__last_operations:
            print(f"Операция: {operation['id']}\n"
                  f"{self.__date_reversed(operation['date'])} {operation['description']}\n"
                  f"{self.__check_from_operation(operation)}"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
                  f"Статус: {self.__check_state(operation['state'])}\n")
