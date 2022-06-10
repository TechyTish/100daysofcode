#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

starting_bill = float(input("What was the total bill? £"))

percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

tips = ((percentage / 100) * starting_bill)

bill_and_tips = starting_bill + tips

split_no = int(input("How many people to split the bill? "))

final_bill = (round(bill_and_tips / split_no, 2))

print(f"Each person should pay: £{final_bill}")
