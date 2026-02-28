def main():
    due = 50
    while due >0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: ")) 
        if coin in (25,10,5):
            due = due - coin 
        else:
            print("please insert right coin")
    owed = abs(due)#abs函数直接计算出绝对值 
    print(f"Change Owed: {owed}")

if __name__ == "__main__":
    main()