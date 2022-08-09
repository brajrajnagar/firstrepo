'''
Dictionary (or dict) is a way to store data just like a list, but instead of using only
numbers to get the data, you can use almost anything. This lets you treat a dict
like it's a database for storing and organizing data.
'''

from cmath import pi


stuff = {'name' : 'Rahgir', 'Age' : 39 }
instuff = {'Rahgir' : 'Male name' , 39 : 'Just a Number'}
print(stuff['name'])
print(stuff)
print('-'*10)
# Adding new data in dict
stuff['Hieght'] = 174
# You can also use numbers to denote the data
stuff[1] = 'Wow'
# Deleting data fro dict
del stuff['Age']
print(stuff)
print('-'*10)
# printing all the info of dict
for i, j in list(stuff.items()):
    print(f'{i} {j} in the stuff Dictionary.')
print('-'*10)
# getting perticular item from dict
nm = stuff.get('name')
# Adding condition incase data does not exist in dictionary
ag = stuff.get('Age', 'Does not exist')
print(f'Name: {nm} Age is {ag}')