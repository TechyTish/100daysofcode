# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#round height to 2 decimal places
height_result = float(height) ** 2
weight_result = int(weight)

#make result an integer
bmi_result = int(weight_result / height_result)

#create an empty string
bmi_category = ""

#if true
if bmi_result < 18.5:
  bmi_category = "underweight"
#else if between 18.5 and 25
elif bmi_result < 25:
  bmi_category = "normal weight"
#else if between 25 and 30
elif bmi_result < 30:
  bmi_category = "slightly overweight"
#else if between 30 and 35
elif bmi_result < 35:
  bmi_category = "obese"
#else if over 35
else:
  bmi_category = "clinically obese"

print(f"Your BMI is {bmi_result}, and you are {bmi_category}!")
