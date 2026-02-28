def main():
    time = input("What time is it?")

    d_time = convert(time)

    if 7 <= d_time <= 8:
        print("breakfast time")
    elif 12 <= d_time <= 13:
        print("lunch time")
    elif 18 <= d_time <= 19:
        print("dinner time")


def convert(time):
    hour,minute = time.split(":")
    f_h = float(hour)
    f_m = float(minute)
    d_m = f_m / 60

    return (f_h + d_m)


if __name__ == "__main__":
    main()