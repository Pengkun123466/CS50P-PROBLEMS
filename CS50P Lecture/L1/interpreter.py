"""calculate = input("What's your calculate")

x,y,z = calculate.split(" ")
f_x = float(x)
f_z = float(z)
if y in ("+","-","*","/"):
    if y == "+":
        result = f_x + f_z
    elif y == "-":
        result = f_x - f_z
    elif y == "*":
        result = f_x * f_z
    elif y == "/":
        result = f_x / f_z
    print(f"{result:.1f}")
else:
    print("It's not a symple Calculation symbols")"""

calculate = input("What's your calculate")

x,y,z = calculate.split(" ")
f_x = float(x)
f_z = float(z)
result = None

match y:
    case "+":
        result = f_x + f_z
    case "-":
        result = f_x - f_z
    case "*":
        result = f_x * f_z
    case "/":
        result = f_x / f_z
    case _:
        print("It's not a symple Calculation symbols")
if result is not None:
    print(f"{result:.1f}")