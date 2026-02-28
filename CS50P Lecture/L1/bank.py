"""greet = input("Greeting:").strip().lower()

capital_greet = greet[0]

if greet == "hello":
    print("0$")
elif capital_greet == "h":
    print("20$")
else:
    print("100$")"""
#缺陷：hello判断过于严格，hello world开头也是hello却会定义为20$
#改进：切片前5个字母是否为hello

greet = input("Greeting:").strip().lower()

if greet[0:5] == "hello":
    print("0$")
elif greet[0:1] == "h":
    print("20$")
else:
    print("100$")