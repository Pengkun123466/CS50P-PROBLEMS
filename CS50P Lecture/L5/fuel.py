def main():
    while True:
        try:
            fractions = input("Fractions: ")
            percentage = convert(fractions)
        except ValueError:
            continue
        except (ValueError, ZeroDivisionError):
            continue
        break
    fuel = gauge(percentage)
    print(f"{fuel}")

def convert(fraction:str) :
    X,Y = fraction.split("/")
    X = int(X)
    Y = int(Y)

    if Y == 0:
        raise ZeroDivisionError
    elif X < 0 or Y < 0 or X > Y:
        raise ValueError
    
    percent = round(X / Y * 100)
    return percent 

def gauge(percentage:int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()