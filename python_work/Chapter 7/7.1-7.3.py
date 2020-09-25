'''7.1'''
print('7.1\n')


def rental_car():
    message = input('What kind of car are you looking for? ')
    print(f'Let me see if I can find you a {message}.')


# rental_car()


'''7.2'''
print('7.2\n')


def restuarant_seating():
    message = input('How many people will be dinning today? ')
    message = int(message)

    if message <= 8:
        print('Your table is ready.')
    else:
        print("I'm sorry, you will have to wait for a table.")


# restuarant_seating()


'''7.3'''
print('7.3\n')


def multiples_of_ten():
    message = input(
        "Give me a number and I'll tell you if it is a multiple of 10. ")
    message = int(message)

    if message % 10 == 0:
        print(f'\nThe number {message} is a multiple of 10')
    else:
        print(f'\nThe number {message} is not a multiple of 10')


multiples_of_ten()
