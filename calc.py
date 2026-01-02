import tkinter as tk
'''imports tkinter modle
tk is an alias for easy access'''

#buttin click handler
def press(v):
    entry.insert(tk.END, v)
    '''called when a number or operator button is clicked 
    inserts the pressed value at the end of entry widget'''

def clear():
    entry.delete(0, tk.END)
    '''clear the calculator screen deletes all characters from index 0 to end'''

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1,tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")


#main window creation
root = tk.Tk()  #creates the main aplication window
root.title("Calculator")  # sets the window title
root.configure(bg="#1e1e1e")  #sets the background color
root.resizable(False, False)  #disables resizing of window


#entry widget(display screen)

entry = tk.Entry(
    root,
    font=("Times new roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)

'''text input field
acts as a calculator display
right-aligned for better claculaton look'''

entry.grid(row=0, column=0, columnspan=4, padx=12, ipadx=10)

''' places entry at top 
colspan = 4 makes it streach across 4 columns'''

#button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
'''represents calculator buttons 
stored in list to reduce repetitive code'''

#dynamic button creation
r = 1
c = 0
'''rows and columns counters for grid layput'''

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)

    ''' if button is "=' call calc()
    otherwise, call press() with the button value
    lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        command=cmd,  #these three lines creates a button widget
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/=" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        r += 1
        c = 0
        '''moves to next row after 4 buttons'''

#clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#ff3b3b",
    fg="white",
    bd=0,
    width=15,
    height=2
).grid(row=r, column=0, columnspan=2, pady=8)

tk.Button(
    root,
    text="B",
    command=backspace,
    font=("Calibri", 14),
    bg="#a5acaf",
    fg="white",
    bd=0,
    width=15,
    height=2
).grid(row=r, column=2, columnspan=2, pady=8)




root.mainloop()
'''keeps the window running listen for 
'''
