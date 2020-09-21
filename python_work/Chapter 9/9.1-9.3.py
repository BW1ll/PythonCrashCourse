'''
Python Crash Course - chapter 9  - Classes

[Try it your self exercises]
'''

# 9.1

class Restaurant:
    '''
     example Restaurant Class in python

    using a generic details a bout Restaurants to build an example class
    '''
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name.upper()} serves {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'{self.restaurant_name.upper()} is open.')

# restaurant = Restaurant("Larry's Pizza", 'Pizza')
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9.2

r1 = Restaurant("larry's pizza", 'pizza')
r2 = Restaurant('olive garden', 'italian')
r3 = Restaurant("homer's", 'southern style\n')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

# 9.3

class User:
    '''
    User Class example

    example python Class for a general user in a general system
    '''
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{self.first_name.title()} {self.last_name.title()}'
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@example.com'
        self.birthday = birthday

    def describe_user(self):
        user_description_message = f'Users current information: \n'
        user_description_message += f'\tUsers name: {self.name}\n'
        user_description_message += f'\tUsers email: {self.email.lower()}\n'
        user_description_message += f'\tUsers birthday: {self.birthday}'
        print(user_description_message)

    def greet_user(self):
        greeting = f'Hello {self.name}\n'
        print(greeting)

u1 = User('brian', 'willis', '03-03-1978')
u2 = User('rob', 'staggs', '03-17-1978')
u3 = User('matt', 'kesterson', '04-17-1978')
u4 = User('sarah', 'willis', '03-27-1978')

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()

u3.describe_user()
u3.greet_user()

u4.describe_user()
u4.greet_user()