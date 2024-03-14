def check_temp(min_value):
  error = "Please enter a number that is more" \
          "than {}".format(min_value)

  try:
    response = float(input("Choose a number: "))

    if response < min_value:
      print(error)

    else:
      return response 

  except ValueError:
    print(error)

#Main Routine 

while True:
  to_check = check_temp(-273)
  print("Success")


def check_temp(self, min_value):

has_error = "no"
error = "Please enter a number that is more than {}".format(min_value)

#check that user has entered a valid number...
try:
  response = self.temp_entry.get()
  response = float(response)

  if response < min_value:
    has_error = "yes"

except ValueError:
  has_error = "yes"

#if the number is invalid, display error message
if has_error == "yes":
  self.temp_error.config(text=error, fg="#9C0000")

else:
  self.temp_error.config(text="You are OK", fg="blue")

#if we have atleast one valid calcutions,
#enable history / export button
  self.to_history_button.config(state=NORMAL)

#if the number is invalid, display error message
if has_error == "yes":
  self.temp_error.config(text=error, fg="#9C0000")

else:
  self.temp_error.config(text="You are OK", fg="blue")

