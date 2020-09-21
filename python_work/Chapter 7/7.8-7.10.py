'''7.8'''
print('7.8\n')


def deli():
    sandwiches = ['club', 'cold cut', 'roast beff', 'BLT']
    finished_sandwiches = []

    while sandwiches:
        current_sandwiches = sandwiches.pop()

        print(f'I have made the {current_sandwiches.title()}')
        finished_sandwiches.append(current_sandwiches)

    print(f'\nThe following sandwiches have been made:')
    for sandwich in finished_sandwiches:
        if sandwich.lower() == 'blt':
            print(f'\tBLT')
        else:
            print(f'\t{sandwich.title()}')


# deli()


'''7.9'''
print('7.9\n')


def pastrami():
    sandwiches = ['club', 'pastrami', 'cold cut', 'pastrami', 'roast beff',
                  'pastrami', 'BLT']
    finished_sandwiches = []

    print(f'We are out of Pastrami!')
    while 'pastrami' in sandwiches:
        sandwiches.remove('pastrami')

    while sandwiches:
        current_sandwiches = sandwiches.pop()

        print(f'I have made the {current_sandwiches.title()}')
        finished_sandwiches.append(current_sandwiches)

    print(f'\nThe following sandwiches have been made:')
    for sandwich in finished_sandwiches:
        if sandwich.lower() == 'blt':
            print(f'\tBLT')
        else:
            print(f'\t{sandwich.title()}')


# pastrami()


'''7.10'''
print('7.10\n')


def vacaton():
    responses = {}

    polling_active = True

    while polling_active:
        name = input('\nWhat is your name? ')
        response = input('Where would you licke to go on vacation? ')

        responses[name] = response

        repeat = input('Would you like to let someone else respond? (yes/no) ')
        if repeat == 'no':
            polling_active = False

    print('\n-------Polling Results-------')
    for name, response in responses.items():
        print(f'{name.title()} would like to vaction in {response.upper()}!')


# vacaton()
