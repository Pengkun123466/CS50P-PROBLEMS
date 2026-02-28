import inflect

def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    name_transfer = p.join(name_list)
    print(f"Adieu, adieu, to {name_transfer}")
    


if __name__ == "__main__":
    main()