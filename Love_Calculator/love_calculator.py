print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Write your code below this line 👇
final_name = name1 + name2
lower_final_name = final_name.lower() 

t = lower_final_name.count('t')
r = lower_final_name.count('r')
u = lower_final_name.count('u')
e = lower_final_name.count('e')
true = t + r + u + e

l = lower_final_name.count('l')
o = lower_final_name.count('o')
v = lower_final_name.count('v')
e = lower_final_name.count('e')
love = l+o+v+e

love_score = int(str(true) + str(love))

# print(love_score)

if love_score <10 or love_score >90:
    print(f"Your love score is {love_score}, You go together like Coke and Mentos!!")
elif love_score <=90 and love_score >=80:
    print(f"Your love score is {love_score}, You both are eternal lovers!!")
elif love_score <80 and love_score >=51: 
    print(f"Your love score is {love_score}, You both are compatible")
elif love_score>= 40 and love_score<=50:
    print(f"Your love score is {love_score}, You are alright together")
else:
     print(f"Your love score is {love_score}")
