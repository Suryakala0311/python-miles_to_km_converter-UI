from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

def calc():
    try:
        user_input = float(user_entry.get())
        result = float(user_input) * 1.60934
        result_label.config(text=result)
    except:
        wrong_label.config(text="Please enter a valid number.")

def refresh():
    result_label.config(text="0")
    user_entry.delete(0, "end")
    wrong_label.config(text="")

wrong_label = Label(text="")
wrong_label.grid(row=0, column=0)

user_entry = Entry(width=8)
user_entry.grid(row=0, column=1, padx=10,pady=10)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

refresh_button = Button(text="Refresh", command=refresh)
refresh_button.grid(row=2, column=0, padx=20, pady=10)

calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(row=2, column=1, padx=20, pady=10)


window.mainloop()
