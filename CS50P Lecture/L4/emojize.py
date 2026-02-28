import emoji

def main():
    text = input("Input: ")
    t_emoji = emoji.emojize(text,language='alias')
    print(t_emoji)

if __name__ == "__main__":
    main()