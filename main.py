import os
from PIL import Image


def ImgFormat(sourceFilePath: str, targetFilePath: str, side_length: int = None):
    """
    图片格式转换Any->ICO
    :param sourceFilePath:
    :param side_length:没有意义，怎样设置，最终出来的还是256x256
    :return:
    """
    img = Image.open(sourceFilePath)
    if side_length is not None:
        img = img.resize((side_length, side_length))
    tmp = os.path.splitext(sourceFilePath)
    root = os.path.dirname(sourceFilePath)
    img.save(targetFilePath)
    print(f"File {targetFilePath} has been saved.")


if __name__ == '__main__':
    from tkinter import filedialog
    import os

    options = {'initialdir': os.getcwd(), 'title': '万能格式转换器Universal Format Kit', 'filetypes': [
        ('图片文件', 'png'),
        ('图片文件', 'jpg'),
        ('图片文件', 'jpeg'),
        ('所有文件', '.*')
    ], 'message': '请选择将进行格式转换的图片：', 'defaultextension': 'png', 'multiple': False, 'typevariable': True}
    # 请求选择文件夹/目录
    # 设置文件对话框会显示的文件类型

    sourceFile = filedialog.askopenfilename(**options)
    print(sourceFile)

    saveOpts = {'initialdir': os.getcwd(), 'title': '万能格式转换器Universal Format Kit', 'filetypes': [
        ('ICO', 'ico'),
        ('PNG', 'png'),
        ('JPEG', 'jpeg'),
    ], 'message': '请选择输出位置和格式：', 'defaultextension': 'ICO'}
    # 设置文件对话框会显示的文件类型
    print("芝麻开门")
    targetFile = filedialog.asksaveasfilename(**saveOpts)
    print(targetFile)
    ImgFormat(sourceFile, targetFile)
