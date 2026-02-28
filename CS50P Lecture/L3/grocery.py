def main():
    list = {}
    while True:
        try:
            item = input().strip().upper()
            list[item] = list.get(item,0) + 1
            
        except EOFError:
            for list_item in sorted(list):
                count = list[list_item]
                print(f"{count} {list_item}")
            break



if __name__ == "__main__":
    main()