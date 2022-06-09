#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
starting_bill = input(float("What was the total bill? £"))

#percentages of tip options
percent_10 = 10
percent_12 = 12
percent_15 = 15

percentage = input(int(f"What percentage tip would you like to give? {percent_10}, {percent_12} or {percent_15}? "))
percentage = int((percentage / 100) * starting_bill)

split_no = input(int("How many people to split the bill? "))

final_bill = round(percentage / split_no) ** 2

print(f"Each person should pay: £{final_bill}")