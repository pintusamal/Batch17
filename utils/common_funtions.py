import json


def read_data_from_input_data(key):
    file_path = r"C:\Users\HP\PycharmProjects\Batch17Project\data\input_data.json"
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data[key]


