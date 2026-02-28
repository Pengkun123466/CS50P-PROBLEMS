def main():
    total = 0
    while True:
        try:
            dish = input("Item: ").lower()
            dish_price = menu(dish)
            total = float(total + dish_price)
            print(f"Total: ${total:.2f}")
        except EOFError:               # 捕获 Control-D (EOF) 信号
            print()
            break
        except KeyError:               # 识别输入键是否在字典内部
            pass


def menu(dish:str) -> int:
    Taqueria_menu ={
    'baja taco': 4.25,
    'burrito': 7.5,
    'bowl': 8.5,
    'nachos': 11.0,
    'quesadilla': 8.5,
    'super burrito': 8.5,
    'super quesadilla': 9.5,
    'taco': 3.0,
    'tortilla salad': 8.0
}
    price = Taqueria_menu[dish]
    return price


if __name__ == "__main__":
    main()