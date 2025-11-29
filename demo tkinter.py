from tkinter import *
root = Tk()
root.geometry("400x250")

Label(root, text="Nhập tên").place(x=20, y=30)
Entry(root).place(x=100, y=30)
Button(root, text="Chào bạn").place(x = 80, y = 80)

Button(root, text = "Ok").place(x = 30, y = 170)
Button(root, text = "Cancel").place(x = 80, y = 170)

root.mainloop()