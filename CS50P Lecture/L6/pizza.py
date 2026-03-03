import sys
from tabulate import tabulate
import csv

def main():
    csv_name = Command_Argument()
    menu_data = transform(csv_name)
    grid = tabulate(menu_data,headers="firstrow",tablefmt="grid")
    print(f"{grid}")


def Command_Argument():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        pass
    
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    return sys.argv[1]

def transform(csv_name:str):
    try:
        menu = []
        with open (csv_name,"r") as file:
            reader = csv.reader(file)

            for row in reader:
                menu.append(row)
        return menu
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()