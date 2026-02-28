from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()#获取所有可用字体
    random_fonts = random.choice(available_fonts)

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f","--front"]:
            sys.exit("Invalid usage")
        if sys.argv[2] not in available_fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])
    elif len(sys.argv) == 1:
        figlet.setFont(font=random_fonts)
    else:
        sys.exit("Invalid usage")
    text = input("Input: ")
    art = figlet.renderText(text)
    print(art) 
    
if __name__ == "__main__":
    main()