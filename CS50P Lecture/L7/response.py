from validator_collection import checkers

def main():
    print(validate_email(input("What's your email address? ")))

def validate_email(s: str) -> str:
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()