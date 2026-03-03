import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    code_name = sys.argv[1]

    try:
        with open(f"{code_name}","r") as file:
            code_line = 0
            for line in file:
                if line.lstrip() == "":
                    pass
                elif line.lstrip().startswith == "#":
                    pass
                else:
                    code_line += 1
        print(f"{code_line}")
    except FileNotFoundError:
        sys.exit("File does not exist")
    
if __name__ == "__main__":
    main()