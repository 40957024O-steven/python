import tkinter as tk

def button_click():
    label.config(text="Hello, World!")


window = tk.Tk()# 创建主窗口

window.geometry("300x200")# 设置窗口尺寸

window.title("My Window")# 设置窗口标题

label = tk.Label(window, text="Click the button!")# 创建标签

et = tk.Entry(window)#使用者輸入東西

button = tk.Button(window, text="Click Me!", command=button_click)# 创建按钮

# 添加标签和按钮到窗口
label.pack()
button.pack()
et.pack()

window.mainloop()# 运行窗口