import csv

class StringUtils:
    def __init__(self, string):
        self.string = string

    def toUpper(self):
        return self.string.upper()

    def toToggle(self):
        result = ""
        for i, char in enumerate(self.string):
            if i % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
        return result

    def generateCSV(self,filename="output.csv"):
        f = open(filename, "w")
        setences = ""
        for i in self.string:
            setences += f'{i},'
        f.write(setences[:-1])
        f.close()
        return filename