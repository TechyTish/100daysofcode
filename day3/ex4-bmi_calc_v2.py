# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_result = float(height) ** 2
weight_result = int(weight)

bmi_result = round(weight_result / height_result ** 2)

bmi_category = ""

if bmi_result < 18.5:
  bmi_category = "underweight"
elif bmi_result < 25:
  bmi_category = "normal weight"
elif bmi_result < 30:
  bmi_category = "slightly overweight"
elif bmi_result < 35:
  bmi_category = "obese"
else:
  bmi_category = "clinically obese"

print(f"Your BMI is {bmi_result}, and you are {bmi_category}!")
