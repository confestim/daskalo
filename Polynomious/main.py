from tkinter import *
import tkinter as tk
import tkinter.messagebox



color = "#3e4447"
window = Tk()
window.title("XImath Client 1.0")
window.configure(bg=color)
window.geometry("500x500")


def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()

class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __repr__(self):

        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x ** index
        return res

def center(win):

    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def calculateIt():
    endList = []
    mathCoef = E1.get()
    coeffs = map(int, mathCoef.split(','))

    p = Polynomial(*coeffs)

    for x in range(len(list(coeffs))):
       result = x, p(x)
       endList.append(result)

    print(endList)
    endResult = ' '.join(map(str, endList))
    print(endResult)
    tkinter.messagebox.showinfo("Result", endResult)
    print(mathCoef)
# dobavi delene A(x):B(x)=N(x) + R(x)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = Frame(window, width=400, height=128, background=color)
frame.pack(padx=50, pady=50)

img = PhotoImage(file='resources/label.png')
make_label(frame, img)
E1 = Entry(window, bd=5, font=("Helvetica", 20), bg="white",justify='center')
E1.pack(padx=50, pady=50)
photo = PhotoImage(file="resources/button.png")
B1 = Button(window, command=calculateIt, image = photo, height=40, width= 100, compound="c", fg=color)
B1.pack(padx=5, pady=5)
center(window)
window.mainloop()
