from tkinter import *

window = Tk()
window.geometry("300x200")
window.title("My first Tkinter")

#label : 文字表現
label1 = Label(window, text="こんにちは")
#配置方法
# 1.pack() : 自動で上から下に順番に配置
label1.pack()

def button_click():
    label2.config(text="良い年を", bg="white")

#Button
button1 = Button(window, text="押してください", command=button_click)
button1.pack()

label2 = Label(window, text="", font=(30), fg="blue")
label2.pack()



window.mainloop()