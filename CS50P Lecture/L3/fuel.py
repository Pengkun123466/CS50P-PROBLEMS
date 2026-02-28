def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fuel_per = fuel(fraction)
            if fuel_per <= 1:
                print("E")
            elif fuel_per >= 99:
                print("F")
            else:
                print(f"{fuel_per}%")
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error:{e}")
        
        

def fuel(fraction:str) -> int:
    molecular,denominator = fraction.split("/")
    molecular_int = int(molecular)
    denominator_int = int(denominator)

    if molecular_int < 0 or denominator_int < 0:
        raise ValueError("Inputs cannot be negative")
    if molecular_int > denominator_int:
        raise ValueError("Numerator cannot be greater than denominator")

    percent = molecular_int / denominator_int * 100

    return percent
    

if __name__ == "__main__":
    main()