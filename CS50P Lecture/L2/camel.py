def main():
    camel = input("camelCase:")
    snake = camel_case(camel) 
    print(f"snakeCase:{snake}")


def camel_case(camel: str) -> str:
    case = []
    for letter in camel:
        if letter.isupper():
            case.append("_")
            case.append(letter.lower())
        else:
            case.append(letter)
    return "".join(case)

if __name__ == "__main__":
    main()