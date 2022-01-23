from tkinter import *
from turtle import onclick

root = Tk()
root.geometry("331x497")
root.configure(bg="#272624")
root.resizable(0, 0)
root.title("Calculator")
root.iconbitmap('C:/Users/subhr/OneDrive/Documents/Programs/Python/tkinter/calc.ico')


display_frame =LabelFrame(root)
display_frame.pack()

e = Entry(root, font="Verdana 30", fg="#ffffff", bg="#252626", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
e.insert(0, 0)
e.delete(0, END)
e.pack(expand = True, fill = "both", pady=(115, 0))

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_num)
    e.delete(0, END)

def button_sub():
    first_num = e.get()
    global f_num
    global math
    math = "sub"
    f_num = float(first_num)
    e.delete(0, END)

def button_mul():
    first_num = e.get()
    global f_num
    global math
    math = "mul"
    f_num = float(first_num)
    e.delete(0, END)

def button_div():
    first_num = e.get()
    global f_num
    global math
    math = "div"
    f_num = float(first_num)
    e.delete(0, END)

def button_mod():
    first_num = e.get()
    global f_num
    global math
    math = "mod"
    f_num = int(first_num)
    e.delete(0, END)

def button_root():
    global math
    math = "root"

def button_sqr():
    global math
    math = "sqr"

def button_equal():
    second_num = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + float(second_num))

    if math == "sub":
        e.insert(0, f_num - float(second_num))

    if math == "mul":
        e.insert(0, f_num * float(second_num))

    if math == "div":
        e.insert(0, f_num / float(second_num))

    if math == "mod":
        e.insert(0, f_num % int(second_num))

    if math == "root":
        s_num = int(second_num)
        e.insert(0, s_num**0.5)

    if math == "sqr":
        e.insert(0, int(second_num) * int(second_num))

button_frame =LabelFrame(root, bg="#252626", bd=0)
button_frame.pack()

# Define Buttons
button_0 = Button(button_frame, text="0", padx=32.5, pady=20, command=lambda: button_click(0), bg="#070707", fg="#ffffff")
button_1 = Button(button_frame, text="1", padx=34, pady=20, command=lambda: button_click(1), bg="#070707", fg="#ffffff")
button_2 = Button(button_frame, text="2", padx=32.5, pady=20, command=lambda: button_click(2), bg="#070707", fg="#ffffff")
button_3 = Button(button_frame, text="3", padx=32.5, pady=20, command=lambda: button_click(3), bg="#070707", fg="#ffffff")
button_4 = Button(button_frame, text="4", padx=34, pady=20, command=lambda: button_click(4), bg="#070707", fg="#ffffff")
button_5 = Button(button_frame, text="5", padx=32.5, pady=20, command=lambda: button_click(5), bg="#070707", fg="#ffffff")
button_6 = Button(button_frame, text="6", padx=32.5, pady=20, command=lambda: button_click(6), bg="#070707", fg="#ffffff")
button_7 = Button(button_frame, text="7", padx=34, pady=20, command=lambda: button_click(7), bg="#070707", fg="#ffffff")
button_8 = Button(button_frame, text="8", padx=32.5, pady=20, command=lambda: button_click(8), bg="#070707", fg="#ffffff")
button_9 = Button(button_frame, text="9", padx=32.5, pady=20, command=lambda: button_click(9), bg="#070707", fg="#ffffff")
button_dot = Button(button_frame, text=".", padx=36, pady=20, command=lambda: button_click("."), bg="#070707", fg="#ffffff")
button_add = Button(button_frame, text="+", padx=31.5, pady=20, command=button_add, bg="#161616", fg="#ffffff")
button_sub = Button(button_frame, text="-", padx=33, pady=20, command=button_sub, bg="#161616", fg="#ffffff")
button_mul = Button(button_frame, text="\u00D7", padx=32, pady=20, command=button_mul, bg="#161616", fg="#ffffff")
button_div = Button(button_frame, text="\u00F7", padx=32, pady=20, command=button_div, bg="#161616", fg="#ffffff")
button_mod = Button(button_frame, text="%", padx=32, pady=20, command=button_mod, bg="#161616", fg="#ffffff")
button_root = Button(button_frame, text="\u221ax", padx=29, pady=20, command=button_root, bg="#161616", fg="#ffffff")
button_sqr = Button(button_frame, text="x\u00b2", padx=31, pady=20, command=button_sqr, bg="#161616", fg="#ffffff")
button_equal = Button(button_frame, text="=", padx=31.5, pady=20, command=button_equal, bg="#652428", fg="#ffffff")
button_clear = Button(button_frame, text="C", padx=31.5, pady=20, command=button_clear, bg="#161616", fg="#ffffff")

# Put Buttons on the Screen
button_mod.grid(row=5, column=0)
button_sqr.grid(row=5, column=1)
button_root.grid(row=5, column=2)
button_div.grid(row=5, column=3)

button_7.grid(row=6, column=0)
button_8.grid(row=6, column=1)
button_9.grid(row=6, column=2)
button_mul.grid(row=6, column=3)

button_4.grid(row=7, column=0)
button_5.grid(row=7, column=1)
button_6.grid(row=7, column=2)
button_sub.grid(row=7, column=3)

button_1.grid(row=8, column=0)
button_2.grid(row=8, column=1)
button_3.grid(row=8, column=2)
button_add.grid(row=8, column=3)

button_dot.grid(row=9, column=0)
button_0.grid(row=9, column=1)
button_clear.grid(row=9, column=2)
button_equal.grid(row=9, column=3)

root.mainloop()
