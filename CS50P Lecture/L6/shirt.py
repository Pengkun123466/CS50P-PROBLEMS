import sys
import os
from PIL import Image, ImageOps

def main():
    check_argv()
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    output_image = photoshop(input_image,output_image)

def check_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
#.jpg、.jpeg 或 .png
   #if not sys.argv[1].endswith((".jpg",".jpeg",".png")):
   #     sys.exit("Invalid output")
   # if not sys.argv[2].endswith((".jpg",".jpeg",".png")):
   #     sys.exit("Invalid output")

    read_name,read = os.path.splitext(sys.argv[1])
    write_name,write = os.path.splitext(sys.argv[2])
    read = read.lower()
    write = write.lower()
    if not read == write:
        sys.exit("Input and output have different extensions")

    if read not in(".jpg",".jpeg",".png"):
        sys.exit("Invalid output")
    if write not in(".jpg",".jpeg",".png"):
        sys,exit("Invalid output")

def photoshop(input_image,output_image):
    shirt = Image.open("shirt.png")
    try:
        with Image.open (input_image) as photo:
            shirt_size = shirt.size
            photo = ImageOps.fit(photo, shirt_size)
            photo.paste(shirt, shirt)
            photo.save(output_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")
if __name__ == "__main__":
    main()