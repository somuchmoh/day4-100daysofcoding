# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
group = len(names)
random_choice = random.randint(0, group-1)   
#Last index is one less than total since we start counting from 0
banker = names[random_choice]
print(f"{banker} is going to buy the meal today!")