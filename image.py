import os
from PIL import Image
from tkinter import filedialog


def ImgFormat(sourceFilePath: str, targetFilePath: str, side_length: int = None):
    """
    图片格式转换Any->ICO
    :param targetFilePath:
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


def ImageFormatUtils(title: str = '万能图片格式转换器'):
    options = {'initialdir': os.getcwd(), 'title': title, 'filetypes': [
        ('图片文件', 'png'),
        ('图片文件', 'jpg'),
        ('图片文件', 'jpeg'),
        ('所有文件', '.*')
    ], 'message': '请选择将进行格式转换的图片：', 'defaultextension': 'png', 'multiple': False, 'typevariable': True}
    # 请求选择文件夹/目录
    # 设置文件对话框会显示的文件类型

    source_file = filedialog.askopenfilename(**options)
    print(source_file)

    save_opts = {'initialdir': os.getcwd(), 'title': title, 'filetypes': [
        ('ICO', 'ico'),
        ('PNG', 'png'),
        ('JPEG', 'jpeg'),
    ], 'message': '请选择输出位置和格式：', 'defaultextension': 'ICO'}
    # 设置文件对话框会显示的文件类型
    print("芝麻开门")
    target_file = filedialog.asksaveasfilename(**save_opts)
    print(target_file)
    if type(source_file) is not str and type(target_file) is not str:
        ImgFormat(source_file, target_file)
