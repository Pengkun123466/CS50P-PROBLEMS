import random


def main():
    Digits_level = get_level()
    score = 0
    
    for _ in range(10):
        x = generate_integer(Digits_level)
        y = generate_integer(Digits_level)
        mistakes = 0
        for _ in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
                answer = int(x + y)
                if z == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
            except ValueError:
                print("EEE")
                mistakes += 1
                continue
        if mistakes ==3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level <4 :
                break
        except ValueError:
            continue
    return level

def generate_integer(Digits_level:int) -> int:
    if Digits_level == 1:
        Integer = random.randint(0,9)
    elif Digits_level == 2:
        Integer = random.randint(10,99)
    else:
        Integer = random.randint(100,999)
    return Integer


if __name__ == "__main__":
    main()