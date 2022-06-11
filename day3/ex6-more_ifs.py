print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
  #nested if statement
  if age < 12:
    print("Child tickets are £5.")
  elif age <= 18:
    print("Youth tickets are £9.")
  else:
    print("Adult tickets are £15.")
else:
  print("You are not tall and/or old enough to ride.")