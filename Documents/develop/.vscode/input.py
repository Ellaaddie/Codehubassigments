Water = input("How many sachet are in one bag: ")
Cost = input("How much does a bag cost: ")
Fivebags = input("Cost of 5 bags: ")
print(f'''The price of a bag of water is {Cost} 
There are {Water} in one bag. If you want to buy 5 it will cost you {Fivebags}''')
drink = input ("How much is a bottle of drink: ")
totalamount = int(Fivebags) + int(drink)
print(f'I bought five bags of water and a drink from Ronke. In total I spent {totalamount}')