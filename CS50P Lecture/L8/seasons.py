from datetime import date
import inflect
import sys

#words = p.number_to_words(12345,andword="")数字转文字
#classmethod date.fromisoformat(date_string)
#返回一个对应于以任何有效 ISO 8601 格式给出的 date_string 的 date
def main():
    #p = inflect.engine()
    birth_date = input("Date of Birth: ")
    minutes_int = get_minutes(birth_date)
    minutes_str = convert_to_words(minutes_int)
    print(f"{minutes_str}")

def get_minutes(birth_date:str) -> int:
    try:
        bitrth_time = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")

    today_time = date.today()

    past_time = today_time - bitrth_time
    minutes = past_time.days * 24 * 60
    return minutes

def convert_to_words(minutes_int: int) -> str:
    p = inflect.engine()
    words = p.number_to_words(minutes_int, andword="")
    words = words.replace(",", "")
    words = words.capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()