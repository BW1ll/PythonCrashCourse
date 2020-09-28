with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())
print(contents)

filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object2:
    lines = file_object2.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(f'{pi_string[:52]}...')
    print(len(pi_string))

with open(filename) as file_object3:
    lines = file_object3.readlines()
    pi_string2 = ''
    for line in lines:
        pi_string2 += line.strip()

birthday = input('Enter your birthday , in the form mmddyy: ')
if birthday in pi_string2:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi')