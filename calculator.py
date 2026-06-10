from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get().replace("^", "**"))
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("CSC426 Calculator")
root.geometry("300x400")

entry = Entry(root, font=("Arial", 20))
entry.pack(fill=BOTH, padx=10, pady=10)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','%','^','+'],
]

for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill=BOTH)
    for btn in row:
        Button(frame, text=btn,
               command=lambda b=btn: click(b),
               font=("Arial",16)).pack(side=LEFT, expand=True, fill=BOTH)

Button(root, text="=", command=calculate,
       font=("Arial",16)).pack(fill=BOTH)

Button(root, text="C", command=clear,
       font=("Arial",16)).pack(fill=BOTH)

root.mainloop()