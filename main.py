import sys
from string_utils import StringUtils

if __name__ == "__main__":
    args = sys.argv
    lenArgs = len(args)
    text = ""
    if(lenArgs > 2):
        exit("only accept 1 arguments")
    if(lenArgs > 1):
        text = sys.argv[1]
    else:
        text = input("Input string : ")

    string = StringUtils(text)

    # Get string to upper
    print(string.toUpper())

    # Get string to toggle case
    print(string.toToggle())

    # Create CSV
    csv_file = string.generateCSV()
    print("CSV created:", csv_file)