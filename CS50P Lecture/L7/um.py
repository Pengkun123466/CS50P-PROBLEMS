import re

def main():
    print(count(input("Text: ")))

def count(s:str) -> int:
    s = s.lower()
    match = re.findall(r"\bum\b",s)
    num = len(match)
    return num

if __name__ == "__main__":
    main()