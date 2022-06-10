# 🚨 Don't change the code below 👇
from multiprocessing.context import assert_spawning


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_result = float(height) ** 2
weight_result = int(weight)

bmi_result = int(weight_result / height_result)

bmi_category = ""

if bmi_result < 18.5:
  bmi_category = "underweight"

if bmi_result > 18.5 < 25:
  bmi_category = "normal weight"

if bmi_result > 25 < 30:
  bmi_category = "slightly overweight"

if bmi_result > 30 < 35:
  bmi_category = "obese"

if bmi_result > 35:
  bmi_category = "clinically obese"

print(f"Your BMI is {bmi_result}, and you are {bmi_category}!")
