print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
crossroad = input("You've stumbled upon a crossroad. Do you want to go \"left\" or \"right\"? \n").lower()
if crossroad == "right":
    print("You have fallen into en sinkhole.")
    print("GAME OVER!")
else:
    print("You've found a lake.")
    lake = input("Do you want to wait for a boat (type \"wait\") of swim across (type \"swim\") \n").lower()
    if lake == "swim":
        print("You have been attacked and eaten by a trout.")
        print("GAME OVER!")
    else:
        print("You see three doors, one red, one blue and one yellow.")
        door = input("Which door do you want to open? \n").lower()
        if door == "red":
            print("You have been burned by fire.")
            print("GAME OVER!")
        elif door == "blue":
            print("You have been washed away by a tidal wave.")
            print("GAME OVER!")
        elif door == "yellow":
            print("You have found the treasure!")
            print("You win!")
        else:
            print("GAME OVER!")
