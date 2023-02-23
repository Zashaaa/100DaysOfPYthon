import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

images = [rock, paper, scissors]

user_choice = int(input("What is your choice? Type \"0\" for rock, \"1\" for paper or \"2\" for scissors.\n"))
if (user_choice < 0) or (user_choice > 2):
    print("You chose an invalid number. You lose")
else:
    print(images[user_choice])

    cpu_choice = random.randint(0, 2)

    print("Computer chose: ")
    print(images[cpu_choice])

    if user_choice == cpu_choice:
        print("It's a draw")
    elif (user_choice == 0 and cpu_choice == 1) or (user_choice == 1 and cpu_choice == 2) or (user_choice == 2 and cpu_choice == 0):
        print("You lose")
    else:
        print("You win!")
