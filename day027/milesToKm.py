from tkinter import *

window = Tk()
window.title("Converter")
window.minsize(width=700, height=300)


equal_to = Label(text="is equal to", font=("Ariel", 20, "bold"))
equal_to.grid(column= 0, row=1 ,padx= 25, pady= 25)

miles = Label(text="Miles", font=("Ariel", 20, "bold"))
miles.grid(column=2,row=0)

input = Entry()
input.grid(column=1, row=0)

result = Label(text="0", font=("Ariel", 20, "bold"))
result.grid(column=1, row=1,padx= 25, pady= 25)

km = Label(text="Km", font=("Ariel", 20, "bold"))
km.grid(column=2,row=1 )

def calculate_value():
    user_value = float(input.get())
    converted_value = round(user_value * 1.609)
    result.config(text=converted_value)

calculate_button = Button(text="Calculate", font=("Ariel", 20, "bold"),width=7,height=1,command=calculate_value)
calculate_button.grid(row=2,column=1)


window.mainloop()