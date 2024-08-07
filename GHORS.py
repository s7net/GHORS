import os
from Manger import file

clear = lambda: os.system("cls||clear")


class patient(file):
    def __init__(self, file_name="database.json"):
        super().__init__(file_name)

    def create(self):
        pass



