from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")
window.iconbitmap(r'D:\VS\Python\Class 77 (Currency Converter Project)\icon.ico')
window.resizable(False,False)

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = round(a.convert(amount, cur1, cur2), 2)  # Round the result to 2 decimal places
    l5 = tk.Label(window, text=data, font="Times 20 bold").place(x= 200, y= 280)

############### LABEL ###############

l1 = tk.Label(text="Currceny Converter", font="Times 28 bold").place(x = 78, y = 30)
l2 = tk.Label(window, text="Enter amount here:- ", font="Times 18 bold").place(x=75, y=85)
e1 = tk.Entry(window)

l3 = tk.Label(window, text="Enter currency:- ", font="Times 18 bold").place(x=75, y=130)
e2 = tk.Entry(window)

l4 = tk.Label(window, text="Enter required:- ", font="Times 18 bold").place(x=75, y=170)
e3 = tk.Entry(window)

b1 = tk.Button(window, text="Submit", command=clicked).place(x= 240, y= 230)
e1.place(x=300,y=92)
e2.place(x=300,y=135)
e3.place(x=300,y=180)

window.mainloop()
