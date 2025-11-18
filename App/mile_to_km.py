import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300,150)

mile_input = tkinter.Entry()
mile_input.config(width=6)
mile_input.grid(column=1,row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2,row=0)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

output_km = tkinter.Label()
output_km.grid(column=1,row=1)

output_km_symbol = tkinter.Label(text="Km")
output_km_symbol.grid(column=2,row=1)

def calculate():
    miles = int(mile_input.get())
    miles *= 1.6
    output_km.config(text=str(miles))
calculate_button = tkinter.Button(text="Calculate",width=6,command=calculate)
calculate_button.grid(row=2,column=1)










window.mainloop()