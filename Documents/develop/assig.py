import random
name = ["Tolani", "steve"]
rolls = (1,6)
User = random.choice(name) 
diceroll = random.choice(rolls)
print(User)
if diceroll == 6:
    print('Move to the next step')
if diceroll == 1:
    print('Drop dice, end game')