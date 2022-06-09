# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

final_age = 90
days = 365
weeks = 52
months = 12
age_in_int = int(age)

#how many total days to live 90 years
age_days = ((final_age - age_in_int) * days)
#how many total weeks to live 90 years
age_weeks = ((final_age - age_in_int) * weeks)
#how many total months to live 90 years
age_months = ((final_age - age_in_int) * months)

print(f"you have {age_days} days, {age_weeks} weeks, and {age_months} months left until you are {final_age} years old.")