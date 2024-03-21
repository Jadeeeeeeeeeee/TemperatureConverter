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

    #Conversion, help and history / export buttons
    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    self.to_help_button = Button(self.button_frame,
                                   text="Help / Info",
                                   bg="#CC6600",
                                   fg=button_fg, width=12,
                                   font=button_font, command=self.to_help)
    self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

  @staticmethod
  def to_help():
    DisplayHelp()

class DisplayHelp:
  def __init__(self):
    backround = "#FFE6CC"

    self.help_box = Toplevel()

    self.help_frame = Frame(self.help_box, width=300, height=200,
                           bg=backround)
    self.help_frame.grid()

    self.help_heading_label = Label(self.help_frame, bg=backround,
                                   text="Help / Info",font="Arial 14 bold")

    self.help_heading_label.grid(row=0)

    help_text = "To use the program, simply enter the temperature " \
    "you wish to convert and then choose convert " \
    "to either degrees Celcius(centigrade) or " \
    "Fahrenheit.. \n\n" \
    "Note that -273 degrees C " \
    "(-459) is absulute zero (the coldest possible " \
    "temperature). If you try to convert a " \
    "temperature that is less than -273 degrees C, " \
    "you will get an error message. \n\n" \
    "To see your" \
    "calculation history and export it into a text " \
    "file, please click the 'History / Export' button"

    self.help_text_label = Label(self.help_frame, bg=backround,
                                text=help_text, wraplength=350, justify="left")
                
                
                                   

    



if __name__ == "__main__":  
  root = Tk()
  root.title("Temperature Converter")
  converter = Converter()
  root.mainloop()
