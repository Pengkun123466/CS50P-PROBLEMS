import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s:str):
#接收一个 str 类型的 HTML 作为输入，提取其中任何作为 iframe 元素的 src 属性值的 YouTube URL
#并返回其更短、可共享的 youtube.com 等效 URL
    youtube = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\"",s)

    if youtube:
        video_id = youtube.group(1)
        return f"https://youtu.be/{video_id}" 
    else:
        return None

if __name__ == "__main__":
    main()