import os
from PIL import Image


def ToICO(image_path: str, side_length: int):
    """
    图片格式转换Any->ICO
    :param image_path:
    :param side_length:没有意义，怎样设置，最终出来的还是256x256
    :return:
    """
    img = Image.open(image_path).resize((side_length, side_length))
    tmp = os.path.splitext(image_path)
    root = os.path.dirname(image_path)
    new_path = os.path.join(root, tmp[0]+'.ico')
    img.save(new_path)
    print(f"File {new_path} has been saved.")


if __name__ == '__main__':
    ToICO("/Users/shadikesadamu/Documents/iniedu/logo.png", 400)
