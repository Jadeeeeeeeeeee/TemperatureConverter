from tkinter import *

class Converter:

  def __init__(self):

    #common format for all buttons
    #Arial size 14 bold, with white text
    button_font = (Family="Arial", "12", "bold")
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
    print("you pressed help")



if __name__ == "__main__":  
  root = Tk()
  root.title("Temperature Converter")
  converter = Converter()
  root.mainloop()
