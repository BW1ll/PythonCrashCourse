'''Python Carsh Course - Chapter 10'''

# 10.1

with open('text_files/tys10.1.txt') as file_object:
    contents = file_object.read()
print(contents)

filename = 'text_files/tys10.1.txt'
with open(filename) as file_object2:
    lines = file_object2.readlines()
    for line in lines:
        print(line.rstrip())

with open(filename) as file_object2:
    for line in file_object2:
        print(line.rstrip())


# 10.2
print('\n')

with open('text_files/tys10.1.txt') as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'C+'))

filename = 'text_files/tys10.1.txt'
with open(filename) as file_object2:
    lines = file_object2.readlines()
    for line in lines:
        print(line.replace('Python', 'JavaScript').rstrip())

with open(filename) as file_object2:
    for line in file_object2:
        print(line.replace('Python', 'Java').rstrip())
