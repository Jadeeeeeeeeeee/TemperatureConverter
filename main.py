from tkinter import *

class Converter:

   def __init__(self):

    #common format for all buttons
    #Arial size 14 bold, with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"

    # Set up the GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Label(self.temp_frame, text = "Temperature", font = ("Arial", "16", "bold"))
    
    self.temp_heading.grid(row=0)

    instructions = "Please enter a temperature below and" \
                   "then press one of the buttons to convert " \
                   "it from centigrade to Fahrenheit."

    self.temp_instructions = Label(self.temp_frame, text=instructions, wraplength=250, width=40, justify="left" )

    self.temp_instructions.grid(row=1)

    self.temp_entry = Entry(self.temp_frame,
                           font=("Arial", "14"))

    self.temp_entry.grid(row=2, padx=10, pady=10)

    error = "Please enter a number"
    self.temp_error = Label(self.temp_frame, text=error,
                           fg="#9C0000")
    self.temp_error.grid(row=3)

    #Conversion, help and history / export buttons
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_celcius_button = Button(self.button_frame,
                                   text="To Celcius",
                                   bg="#990099",
                                   fg=button_fg,
                                   font=button_font)
    self.to_celcius_button.grid(row=0, column=0)

    self.to_farenheit_button = Button(self.button_frame,
                                   text="To Farenheit",
                                   bg="#009900",
                                   fg=button_fg,
                                   font=button_font)
    self.to_farenheit_button.grid(row=0, column=1)
        


if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()


