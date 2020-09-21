nums = {
    'sarah' : 30,
    'matt' : 16854,
    'sasha' : 13,
    'rob' : 31,
    'me' : 69
}


for k, v in nums.items() :
    print (k, v)


people = ['sarah', 'matt', 'sasha', 'rob', 'me']
for people in nums.keys():
    if people == 'me':
        print(f'My favorite number is {v}')
    else:
        print(f"{people.title()}'s favorit numbe is {v}")    