def main():
   while True:
        try:
            date = input("Date: ")
            ISO_date = ISO(date)
            print(f"{ISO_date}")
            break
        except ValueError:
            pass


def ISO(date:str) -> int:
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    if "/" in date:
        m,d,y = (date.split("/"))
        month = int(m)
        day = int(d)
        year = int(y)
        if day > 31 or month > 12:
            raise ValueError
        return(f"{year}-{month:02}-{day:02}")
    elif "," in date:
        date = date.replace(",","")
        month,day,year = (date.split(" "))
        if month in months:
            month = months.index(month) + 1
            day = int(day)
            year = int(year) 
            if day > 31 or month > 12:
                raise ValueError   
            return(f"{year}-{month:02}-{day:02}")
        else:
                raise ValueError
    else:
        return ValueError
    

if __name__ == "__main__":
    main()