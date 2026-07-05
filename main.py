from src.reader.csv_reader import csv_reader
from src.reader.sheets_reader import read_spreadsheet


def main():
    #print(csv_reader("./expenses.csv"))
    print(read_spreadsheet())

if __name__ == "__main__":
    main()