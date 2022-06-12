print("Welcome to the Silver Key game!")
print("Your mission is to find the silver key behind 1 of the doors!")

print("Ok, please take a seat in the chair")

print('''
        .-===-.
        | . . |
        | .'. |
       ()_____()
       ||_____||
        W     W
 ''')

print('''
    /|                /|              /|          
   / |               / |             / |
  /__|______        /__|______      /__|______
  |  __  __  |     |  __  __  |     |  __  __  |
  | |  ||  | |     | |  ||  | |     | |  ||  | |
  | |  ||  | |     | |  ||  | |     | |  ||  | |
  | |__||__| |^    | |__||__| |^    | |__||__| |^
  |  __  __()|     |  __  __()|     |  __  __()| 
  | |  ||  | +`    | |  ||  | +`    | |  ||  | +` 
  | |  ||  | |     | |  ||  | |     | |  ||  | | 
  | |  ||  | |     | |  ||  | |     | |  ||  | |
  | |__||__| |     | |__||__| |     | |__||__| |
  |__________|     |__________|     |__________|  

  -- DOOR 1 --     -- DOOR 2 --     -- DOOR 3 --
''')

#start the inputs
door_selection = int(input("Which door would you do you think the key is behind, 1, 2 or 3?: "))

#create an empty string 
option = str("").lower()

exit = str("Key not found, you have failed the game!")


if door_selection == 1:
  option = input("Oh no! The room is shaking, do you want to WAIT or EXIT?: ")
  if option == "wait":
    print("Well done for waiting, you guessed correctly and found the Silver Key!")
  else:
    print(exit)
elif door_selection == 2:
  option = input("Ok, there is another door, do you want to enter? Y or N: ")
  if option == "Y":
    print("Ok you have entered door 4... please wait.")
    print(exit)
  else:
    print(exit)
else:
  print("You got eaten by a bear!")
  print(exit)
