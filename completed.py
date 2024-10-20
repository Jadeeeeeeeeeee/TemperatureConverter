from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    def check_temp(self, min_value):
        has_error = "no"
        error = "Please enter a number that is more than {}".format(min_value)

        # Check that user has entered a valid number...
        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"
        else:
            self.var_has_error.set("no")
            self.to_history_button.config(state=NORMAL)
            return response

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    def temp_convert(self, min_val):
        to_convert = self.check_temp(min_val)
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        elif min_val == -459:
            to_convert = float(to_convert)
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"

        else:
            to_convert = float(to_convert)
            answer = to_convert * 1.8 + 32
            from_to = "{} C{} is {} F{}"

        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)
            feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
            self.var_feedback.set(feedback)
            self.all_calculations.append(feedback)
            self.update_history_button_state()

        self.output_asnwer()

    def output_asnwer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")
        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)

    def to_history(self):
        with open("conversion_history.txt", "w") as file:
            for calculation in self.all_calculations:
                file.write(calculation + "\n")

    def create_history_button(self):
        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg="#FFFFFF",
                                        font=("Arial 12 bold"),
                                        width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    def update_history_button_state(self):
        if self.all_calculations:
            self.to_history_button.config(state=NORMAL)
        else:
            self.to_history_button.config(state=DISABLED)

    def __init__(self):
        self.var_feedback = StringVar()
        self.var_feedback.set("")
        self.var_has_error = StringVar()
        self.var_has_error.set("no")
        self.all_calculations = []

        button_font = ("Arial 12 bold")
        button_fg = "#FFFFFF"

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature",
                                  font=("Arial 16 bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and" \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250,
                                       width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial 14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame, text="", fg="#9C0000")
        self.output_label.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        width=12,
                                        font=button_font,
                                        command=lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="To Fahrenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           width=12,
                                           font=button_font,
                                           command=lambda: self.temp_convert(-273))
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     width=12,
                                     font=button_font,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.create_history_button()

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        background = "#FFE6CC"

        self.help_box = Toplevel()
        partner.to_help_button.config(state=DISABLED)
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        bg=background,
                                        text="Help / Info",
                                        font="Arial 14 bold")
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit. \n\n" \
                    "Note that -273 degrees Celsius " \
                    "(-459 Fahrenheit) is absolute zero (the coldest possible " \
                    "temperature). If you try to convert a " \
                    "temperature that is less than -273 degrees Celsius, " \
                    "you will get an error message. \n\n" \
                    "To see your" \
                    "calculation history and export it into a text " \
                    "file, please click the 'History / Export' button"

        self.help_text_label = Label(self.help_frame,
                                     bg=background,
                                     text=help_text,
                                     wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial 12 bold"),
                                     text="Dismiss",
                                     bg="#CC6000",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    converter = Converter()
    root.mainloop()
