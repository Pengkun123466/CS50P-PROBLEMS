def main():
    text = input("text: ")
    shortext = shorten(text)
    print(f"{shortext}")

def shorten(text:str) -> str:
    re_text = []
    for letter in text:
        if letter.lower() not in ("aeiou"):
            re_text.append(letter)
    return "".join(re_text)

if __name__ == "__main__":
    main()