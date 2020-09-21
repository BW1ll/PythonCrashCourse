'''6.7'''
print('6.7\n')

matt = {
    'first_name': 'matt',
    'last_name': 'mesterson',
    'age': 41,
    'city': 'north nittle nock',
    'state': 'ar'
}

rob = {
    'first_name': 'robert',
    'last_name': 'staggs',
    'age': 41,
    'city': 'benton',
    'state': 'mo'
}

vickie = {
    'first_name': 'victoria',
    'last_name': 'estrada',
    'age': 21,
    'city': 'benton',
    'state': 'ar'
}

people = [matt, rob, vickie]

for person in people:
    print(person)

print()

'''6.8'''
print("6.8\n")

hasel = {
    'owner': 'vickie',
    'animal': 'dog'
}

myrtle = {
    'owner': 'sarah',
    'animal': 'dog'
}

shadow = {
    'owner': 'brian',
    'animal': 'dog'
}

boggie = {
    'owner': 'trenton',
    'animal': 'dog'
}

pets = [hasel, myrtle, shadow, boggie]

for pet in pets:
    print(pet)

print()
'''6.9'''
print("6.9\n")


favorite_places = {
    'rob': ['st. louis', 'memephis'],
    'matt': ['mina', 'marion'],
    'brian': ['heber springs', 'benton', 'van buren']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f'\t{place.title()}')


print()
'''6.10'''
print("6.10\n")

nums = {
    'sarah': [30, 7],
    'matt': [16854, 2, 13],
    'sasha': [13, 21],
    'rob': [31],
    'brian': [69, 99, 3]
}
people2 = ['sarah', 'matt', 'sasha', 'rob', 'brian']

for person2, numbers in nums.items():
    if len(numbers) > 1:
        print(f"{person2.title()}'s favorite numbers are:")
        for num in numbers:
            print(f'\t{num}')
    else:
        print(f"{person2.title()}'s favorite number is:")
        for num in numbers:
            print(f'\t{num}')


print()
'''6.11'''
print("6.11\n")


cities = {
    'west memphis': {
        'county': 'crittenden',
        'population': 24_636,
        'fact': 'Native Americans lived in the Mississippi River Valley\n'
        '\t\tfor at least 10, 000 years, although much of the evidence of their\n'
        '\t\tpresence has been buried or destroyed. The Indians of the\n'
        '\t\tMississippian Period were the last native inhabitants of the\n'
        '\t\tWest Memphis area. Mound City Road, located within the eastern\n'
        '\t\tportion of the West Memphis city limits, has a marker indicating\n'
        '\t\tthat the villages of Aquixo(Aquijo) or Pacaha were in the area.\n'
        '\t\tSeveral mounds are still visible.'},
    'little rock': {
        'county': 'pulaski',
        'population': 197_881,
        'fact': "Little Rock is the capital and most populous city of the U.S. state of Arkansas."},
    'cape girardeau': {
        'county': 'cape girardeau',
        'population': 39_853,
        'fact': 'Community founded January 4, 1793, on a Spanish land grant to Louis Lorimier'}
}

for city, city_info in cities.items():
    print(f'{city.upper()}:')
    county = city_info['county'].title()
    population = city_info['population']
    formated_population = '{:,.0f}'.format(population)
    fact = city_info['fact']
    print(f'\tCounty: {county.title()}')
    print(f'\tPopulation: {formated_population}')
    print(f'\tFact: {fact}')


print()
'''6.12'''
print("6.12\n")


#skipped