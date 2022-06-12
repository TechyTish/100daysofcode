print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
photo_bill = 10

if height >= 120:
  #nested if/elif statement
  if age < 12:
    print("Child tickets are £5.")
    bill = 5
  elif age <= 18:
    print("Youth tickets are £9.")
    bill = 9
  #logical operator
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    print("Adult tickets are £15.")
    bill = 15
    
  wants_photo = input("Do you want a photo taken? Y or N: ")
  if wants_photo == "Y":
    #add photo bill back to original bill
    bill += photo_bill
    print(f"Ok, your final bill is: £{bill}")
  else:
    print(f"Ok your bill is: £{bill}")

else:
  print("You are not tall enough to ride.")