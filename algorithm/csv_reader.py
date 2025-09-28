import csv

class CSVReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        data_array = []
        with open(self.path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data_array.append([float(x) for x in row])

        return data_array