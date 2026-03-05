import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip:str):
#接收一个 IPv4 地址作为 str 类型的输入，如果输入是有效的 IPv4 地址，则返回 True，否则返回 False。
    matches = re.match(r"^([1-9][0-9]*|0)\.([1-9][0-9]*|0)\.([1-9][0-9]*|0)\.([1-9][0-9]*|0)$",ip)
    if matches:
        num1,num2,num3,num4 = matches.groups()
        #num1,num2,num3,num4 = int(matches.groups()) X
        #matches.groups() 吐出来的是一个元组,有四个字符串，不能直接int
    else:
        return False
    
    if 0 <= int(num1) <= 255 and 0 <= int(num2) <= 255 and 0 <= int(num3) <= 255 and 0 <= int(num4) <= 255:
        return True
    else:
        return False

if __name__ == "__main__":
    main()