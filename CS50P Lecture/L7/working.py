import re

def main():
    print(convert(input("Hours: ")))

def convert(s:str) ->str:
    twelve_format = re.search("^(1[0-2]|[1-9])(?::?([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::?([0-5][0-9]))? (PM|AM)$",s)
    #9:00 AM to 5:00 PM
    #09:00 to 17:00
    if twelve_format:
        hour1 = int(twelve_format.group(1))
        minute1 = twelve_format.group(2)
        day1 = twelve_format.group(3)
        hour2 = int(twelve_format.group(4))
        minute2 = twelve_format.group(5)
        day2 = twelve_format.group(6)
        if day1 == "PM" and hour1 != 12:
            hour1 = hour1 + 12
        if day2 == "PM" and hour2 != 12:
            hour2 = hour2 + 12
        if day1 == "AM" and hour1 == 12:
            hour1 = 0
        if day2 == "AM" and hour2 == 12:
            hour2 = 0

        if minute1 == None:
            minute1 = "00"
        if minute2 == None:
            minute2 = "00"
        
        return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()