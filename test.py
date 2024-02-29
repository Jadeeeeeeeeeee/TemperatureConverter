import tkinter as tk

#window = tk.Tk()
#window.title("Hello world")
#window.geometry("300x300")

#hello = tk.Label(text="Temperature Converter")
#hello.pack()
#button = tk.Button(text=" me!")
#button.pack()

#tk.mainloop()



def  __init__(self):
  self.temp_frame.Frame() 
  self.temp.grid()

  self.temp_heading.Label(self.temp_frame,text="Temperature Convertor",
                            font = ("Arial",'16', 'bold' ) )
  self.temp_heading.grid(row=0)

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")
root.mainloop()