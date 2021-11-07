from tkinter import *


def cm_to_inch():
    cm = float(entry_input.get())
    inch = round(cm*0.3937)
    label_result.config(text=f"{cm}cmは{inch}インチです。")
    entry_input.delete(0, END)


window = Tk()
window.title("cm/inch変換プログラム")
window.geometry("250x200")
window.config(padx=30, pady=10)

label_title = Label(window, text="cm/inch 変換", \
    font=("游ゴシック",20,"bold"))
label_title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

entry_input = Entry(window, width=15)
entry_input.focus()
entry_input.grid(column=0, row=1, sticky=E)

label_input = Label(window, text="cm", font=("游ゴシック",10,"bold"))
label_input.grid(column=1, row=1, pady=10, sticky=W)

button = Button(window, text="変換する", fg="pink", bg="black", \
    font=("游ゴシック",10,"bold"), width=15, \
        command=cm_to_inch)
button.grid(column=0, row=2, columnspan=2, pady=10)

label_result = Label(window, text="", font=("游ゴシック",10,"bold"))
label_result.grid(column=0, row=3, columnspan=2)






window.mainloop()