#list
wizard_list = ['bread', 'sugar', 'egg', 'fish', 'plantain', 'beans', 'cornflakes']
print(wizard_list)
print(wizard_list[3])
#select an item out of list
print(wizard_list[2:5])
#add an item to an existing list
wizard_list.append('sausage')
wizard_list.append('stone')
print(wizard_list)
#delete an item
del wizard_list[8]
print(wizard_list)
#Maps in Python
favorite_sports = {'Ralph Williams' : 'Football',
                  'Michael Tippet' : 'basketall',
                  'Edward Elgar' : 'Baseball',
                  'Rebecca Clarke' : 'Netball',
                  'Ethel Smyth' : 'Badminton',
                  'Frank Bridge' : 'Rugby'}
print(favorite_sports)
print(favorite_sports['Rebecca Clarke'])
#delete a value in a map
del favorite_sports['Ethel Smyth']
print(favorite_sports)
#replace a value in a map
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)
#How to combine a list
games = ['running', 'swiming', 'reading', 'cooking']
foods = ['eba', 'okro', 'spaghetti', 'bread', 'indomie']
favorites = games + foods
print(favorites)