class Operations:
    def __init__(self, all_operations):
        self.all_operations = all_operations
        self.__last_operations = self.__set_last_operations()

    def __repr__(self):
        return f"Operations({self.all_operations})"