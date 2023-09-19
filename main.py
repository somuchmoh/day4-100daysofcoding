import random
random_integer = random.randint(1, 10)    #Random integer is generated between 1 and 10 (both inclusive)
print(random_integer)

import my_module
print (my_module.pi)    #imported from another module created by me

random_float = random.random() * 5      #To expand the range from 0 to 1 to 0 to 5 > multiply it by 5
print (random_float)

#Lists
states_of_america = ["Delaware", "Pennsylvania","Hawaii", "New Jersey", "Vermont", "Indiana", "Ohio"]  
#The order in the list is the order it takes everywhere. 
print (states_of_america[0])   #Use square brackets to create the list and get something out of the list
print (states_of_america[-1])  #This prints from the end of the list 

#You can also change an input in the list
states_of_america[2] = "Hawai"
print (states_of_america)  #Changes the spelling from "Hawaii" to "Hawai"

#Add an item to the end of the list >> This is call APPEND 
states_of_america.append("Kansas")
print(states_of_america)

states_of_america.extend(["Virginia", "Georgia"])
print(states_of_america)

print(len(states_of_america))
#There are 10 items in the list but since we start counting from 0 - there will only be 9

#If you print(states_of_america[10]) >> This will give you an error since the last input is #9.

#Nested lists - This is a list inside another list
dirty_dozen = ["Strawberry", "Apple", "Grapes", "Papaya", "Mango", "Watermelon", "Spinach", "Potato", "Cucumber", "Carrot", "Tomato", "Lettuce"]
fruits = ["Strawberry", "Apple", "Grapes", "Papaya", "Mango", "Watermelon"]
vegetables = ["Spinach", "Potato", "Cucumber", "Carrot", "Tomato", "Lettuce"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])   
#This will print "potato" since "vegetables" in the 1st element in the list 'dirty_dozen' and "potato" is the first element in the list 'vegetable'.