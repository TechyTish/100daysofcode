print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
  #nested if statement
  if age >= 18:
    print("You can ride the rollercoaster!")
  else:
    print("Sorry, you have to be over 18 before you can ride.")
else:
  print(":( You are not tall and old enough to ride.")
