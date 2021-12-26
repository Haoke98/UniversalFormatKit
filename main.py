from image import ImageFormatUtils


if __name__ == '__main__':
    import tkinter
    from tkinter import filedialog, messagebox
    import os

    Title = '万能格式转换器Universal Format Kit'

    root = tkinter.Tk()
    root.title(Title)  # 标题
    root.geometry('400x200')  # 窗体大小
    root.resizable(False, False)  # 固定窗体
    tkinter.Button(root, text='图片格式转换', command=ImageFormatUtils).pack()
    root.mainloop()
