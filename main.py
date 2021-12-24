import os
from PIL import Image


def ToICO(image_path: str, side_length: int):
    img = Image.open(image_path).resize((side_length, side_length))
    tmp = os.path.splitext(image_path)
    root = os.path.dirname(image_path)
    new_path = os.path.join(root, tmp[0]+'.ico')
    img.save(new_path)
    print(f"File {new_path} has been saved.")


if __name__ == '__main__':
    ToICO("/Users/shadikesadamu/Documents/iniedu/LOGO/20211219213312 拷贝.png", 256)
