from tkinter import *

window = Tk()
window.title("cm/inch変換プログラム")
window.geometry("250x200")
window.config(padx=30, pady=10)

label_title = Label(window, text="cm/inch 変換", \
    font=("游ゴシック",20,"bold"))
label_title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

entry_input = Entry(window, width=15)
entry_input.grid(column=0, row=1, sticky=E)

label_input = Label(window, text="cm", font=("游ゴシック",10,"bold"))
label_input.grid(column=1, row=1, pady=10, sticky=W)



window.mainloop()