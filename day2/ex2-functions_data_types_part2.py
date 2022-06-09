num_char = len(input("What is your name? "))

#check the type of a var
print(type(num_char))

#type conversion aka type casting
#convert integer to string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

#adds an integer to float
print(70 + float("100.5"))

#adds strings together
print(str(70)+ str(100))