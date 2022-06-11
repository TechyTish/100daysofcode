print("Leap Year Calculator!")
number = int(input("What year do you want to check? "))

#empty string
leap_year_result = ""

if (number % 4) == 0:
  if (number % 100) == 1:
    if (number % 400) == 0:
      leap_year_result = "this is a leap year"
else:
    leap_year_result = "this is a not a leap year"

print(f"Result: {leap_year_result}")