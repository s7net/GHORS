import json
import shutil
from os.path import isfile

class file:
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def copy_database(file_name="database.json", base_db="base_db.json"):
        shutil.copy(base_db, file_name) if not isfile(file_name) else None

    def read_file(self):
        with open(self.file_name) as f:
            return json.loads(f.read(self.file_name))

    def write_file(self, content=None):
        if content is not None:
            with open(self.file_name, "w") as f:
                f.write(content)
                return "Success !"
