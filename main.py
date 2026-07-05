from src.reader.csv_reader import csv_reader


def main():
    print(csv_reader("./expenses.csv"))

if __name__ == "__main__":
    main()