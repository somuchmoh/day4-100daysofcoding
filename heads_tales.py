#Heads or Tales generator 

import random
a = ['Heads', 'Tails']
print(random.choice(a))

#Alternative code
random_side = random.randint (0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")