# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
truescore = 0
lovescore = 0
count_t = name1.lower().count("t")
truescore += count_t
count_t = name2.lower().count("t")
truescore += count_t
count_r = name1.lower().count("r")
truescore += count_r
count_r = name2.lower().count("r")
truescore += count_r
count_u = name1.lower().count("u")
truescore += count_u
count_u = name2.lower().count("u")
truescore += count_u
count_e = name1.lower().count("e")
truescore += count_e
count_e = name2.lower().count("e")
truescore += count_e

count_l = name1.lower().count("l")
lovescore += count_l
count_l = name2.lower().count("l")
lovescore += count_l
count_o = name1.lower().count("o")
lovescore += count_o
count_o = name2.lower().count("o")
lovescore += count_o
count_v = name1.lower().count("v")
lovescore += count_v
count_v = name2.lower().count("v")
lovescore += count_v
count_e = name1.lower().count("e")
lovescore += count_e
count_e = name2.lower().count("e")
lovescore += count_e

truelove_score = str(truescore) + str(lovescore)
int_truelove_score = int(truelove_score)

if int_truelove_score < 10 or int_truelove_score > 90:
    print(f"Your score is {int_truelove_score}, you go together like coke and mentos.")
elif 40 <= int_truelove_score < 50:
    print(f"Your score is {int_truelove_score}, you are alright together.")
else:
    print(f"Your score is {int_truelove_score}.")
