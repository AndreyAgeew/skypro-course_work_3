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