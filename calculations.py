def to_celcius(to_convert):
  answer = (to_convert - 32) * 5/9
  return answer

def to_farenheit(to_convert):
  answer = to_convert * 1.8 + 32
  return answer

to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
  print("{} C is {:.0f} F".format(item, to_farenheit(item)))

print()

for item in to_c_test:
  print("{} F  is {:.0r} C".format(item, to_celcius(item)))