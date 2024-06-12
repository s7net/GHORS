import json


class File:
    def __init__(self, Path="database.json"):
        self.Path = Path

    @staticmethod
    def create(fileName, content="Empty", jsonEncode=False):
        fileName = "database.json" if fileName == None else fileName
        with open(fileName, "w") as f:
            f.write(json.dumps(content)) if jsonEncode == True else f.write(content)
        return f"{fileName} is created !"
    
    def read(self):
        with open(self.Path, "r") as f:
            return json.loads(f.read())

    def write(self, content="Empty"):
        with open(self.Path, "w") as f:
            f.write(json.dumps(content, indent=4))
            return "file edited !"
