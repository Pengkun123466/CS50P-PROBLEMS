def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False  
    if not plate.isalnum(): #isalnum() 的全称是 Is Alpha(betic) OR Numeric包含字母和数字
        return False
    if not plate[0:2].isalpha():
        return False
    i = 0
    while i < len(plate):
        if plate[i].isalpha():
            i += 1
            continue
        if plate[i] == '0':
            return False
        if not plate[i:].isdigit():
            return False
        break
    return True
if __name__ == "__main__":
    main()