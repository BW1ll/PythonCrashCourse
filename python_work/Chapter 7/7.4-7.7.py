'''7.4'''
print('7.4\n')


def pizza_toppings():
    prompt = 'Enter a topping for your pizza:'
    prompt += '\nEnter quit to continue. '

    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(f'\t{message} will be add to your pizza.\n')


# pizza_toppings()


'''7.5'''
print('7.5\n')


def movie_tickets():
    message = 'Enter the age of the person watching the move: '
    message += '\nEnter "quit" to exit: '
    under3 = 'Childerend under 3 are Free '
    under13 = 'This ticket is $10.'
    over12 = 'This ticket is $15.'

    active = True
    while active:
        age = input(message)
        if age.lower() == 'quit':
            active = False
        elif int(age) < 3:
            print(f'\t{under3}\n')
        elif int(age) < 13:
            print(f'\t{under13}\n')
        elif int(age) > 12:
            print(f'\t{over12}\n')


# movie_tickets()


'''7.6'''
print('7.6\n')


def movie_tickets2():
    message = 'Enter the age of the person watching the move: '
    message += '\nEnter "quit" to exit: '
    under3 = 'Childerend under 3 are Free '
    under13 = 'This ticket is $10.'
    over12 = 'This ticket is $15.'

    active = True
    while active:
        age = input(message)
        if age.lower() == 'quit':
            break
        elif int(age) < 3:
            print(f'\t{under3}\n')
        elif int(age) < 13:
            print(f'\t{under13}\n')
        elif int(age) > 12:
            print(f'\t{over12}\n')


# movie_tickets2()


'''7.7'''
print('7.7\n')


def infinity():
    x = 0
    while x < 1:
        print(x)


# infinity()
