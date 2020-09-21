''' 6.1 '''
print(6.1, '\n')
matt = {
    'first_name' : 'Matt',
    'last_name' : 'Kesterson',
    'age' : 41,
    'city' : 'North Little Rock'
}

print(matt['first_name'])
print(matt['last_name'])
print(matt['age'])
print(matt['city'])

''' 6.2 '''
print()
print(6.2, '\n')
nums = {
    'sarah' : 30,
    'matt' : 16854,
    'sasha' : 13,
    'rob' : 31,
    'me' : 69
}
people = ['sarah', 'matt', 'sasha', 'rob', 'me']
#for k, v in nums.items():
#    print(k, v)


for k, v in nums.items():
    if k != 'me':
        print(f"{k.title()}'s favorit number is {v}")
    else:
        print('My favorite number is', nums['me'])


'''6.3'''
print("\n6.3", '\n')

glossary = {
    'Item1:' : 'def1',
    'Item2:' : 'def2',
    'Item3:' : 'def3',
    'Item4:' : 'def4',
    'Item5:' : 'def5'
}

for k, v in glossary.items():
    print(f"{k.upper()}\n {v}")