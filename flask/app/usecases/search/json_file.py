import json

class JsonFileManager:
    def dump_json(self, filename, data):
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_json(self, filename):
        with open(filename, "r") as file:
            return json.load(file)