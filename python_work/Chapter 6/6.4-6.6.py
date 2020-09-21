'''6.4'''
# did 6.4 in the 6.1-6.3.py file

'''6.5'''
print('\n6.5', '\n')

rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'litte red': 'usa'
}

for river, country in rivers.items():
    if country == 'usa':
        print(f"The river {river.title()} is in the country {country.upper()}")
    else:
        print(f"The river {river.title()} is in the country {country.title()}")


print()
for river in rivers:
    print(f'{river.title()}')


print()
for country in rivers.values():
    if country == 'usa':
        print(f'{country.upper()}')
    else:
        print(f'{country.title()}')


'''6.6'''
print('\n6.6', '\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'sarah', 'edward', 'brian', 'matt', 'phil', 'rob']

for person in people:
    if person in favorite_languages.keys():
        print(f'Thank you {person.title()} for taking the poll!')
    else:
        print(f'{person.title()}, please take our poll!')
