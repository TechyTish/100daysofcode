print("Leap Year Calculator!")
number = int(input("What year do you want to check? "))

#empty string
leap_year_result = ""

#nested if statmeent
if (number % 4) == 0:
  leap_year_result = "leap year"
  if (number % 100) == 1:
    leap_year_result = "leap year"
    if (number % 400) == 0:
      leap_year_result = "leap year"
else:
  leap_year_result = "not a leap year"

print(f"Result: {leap_year_result}")