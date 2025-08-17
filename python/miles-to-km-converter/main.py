from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

def calculate():
    miles_number = miles_entry.get()
    km_number = int(miles_number) * 1.60934
    km_label.config(text=km_number)

miles_entry = Entry(width=10)
miles_entry.grid(column=1,row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)

km_label_inv = Label(text="is equal to", font=("Arial", 24, "bold"))
km_label_inv.grid(column=0,row=1)
km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(column=1,row=1)
km_label_title = Label(text="Km", font=("Arial", 24, "bold"))
km_label_title.grid(column=2,row=1)

miles_label_title = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label_title.grid(column=2,row=0)

window.mainloop()