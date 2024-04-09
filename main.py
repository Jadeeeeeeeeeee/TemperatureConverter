#Get data from user and store it in a list,then
#display the most recent three entries nicely

#set up empty list
all_calculations = []
MAX_CALCS = 5

#Get items of Data
get_item = ""
while get_item != "xxx":
  get_item = input("Enter an item: ")

  if get_item == "xxx":
    break

  all_calculations.append(get_item)

all_calculations.reverse()

#Show that everything  made it to the list
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 5 ***")
for item in range(0, 5):
  print(all_calculations[item])

print()

#print items starting at the END of the list
if len(all_calculations) >= MAX_CALCS:
  print()
  print("*** Most Recent ***")
  for item in range(0, MAX_CALCS):
    print(all_calculations[len(all_calculations) - item - 1])

else:
  print()
  print("*** Items from Newest to 0ldest ***")
  for item in all_calculations:
    print(all_calculations[len(all_calculations) - item - 1])