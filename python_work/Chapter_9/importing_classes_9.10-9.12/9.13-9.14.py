'''
Python Crash Course - chapter 9  - Classes

[Try it your self exercises]
'''


from random import choice, randint

# 9.13

d6 = list(range(1,7))
d10 = list(range(1,11))
d20 = list(range(1,21))

def roll_die(dice):
    '''A dice roll generator '''
    count = 0
    while count < 10:
        roll = choice(dice)
        count += 1
        print(f'Die roll {count}: {roll}')
    print()

# roll_die(d6)
# roll_die(d10)
# roll_die(d20)


# 9.14


'''Generat lottory wining numbers'''
lot_items = ['A', 'B', 'C', 'D', 'E', '52', '52', '18', '30', '73', '14', '11', '78', '41', '82']
def wining_number():
    wining_numbers = []
    count = 0
    while count < 4:
        wining_numbers.append(choice(lot_items))
        count += 1
    print(f'The wining nubers are: {wining_numbers}')
    return wining_numbers

wining_number()