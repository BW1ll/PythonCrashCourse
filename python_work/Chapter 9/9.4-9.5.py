'''
Python Crash Course - chapter 9  - Classes

Try it your self exercises
'''

# 9.4

class Restaurant:
    '''
     example Restaurant Class in python

    using a generic details a bout Restaurants to build an example class
    '''
    def __init__(self, restaurant_name, cuisine_type):
        '''initialize attributes to describe restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''return a neatly formated description of restaurant'''
        print(f'{self.restaurant_name.upper()} serves {self.cuisine_type.title()}')

    def open_restaurant(self):
        '''returns restaurant is open message'''
        print(f'{self.restaurant_name.upper()} is open.')

    def set_number_served(self, set):
        ''' returns message with the number of people served'''
        self.number_served = set
        print(f'{self.restaurant_name.upper()} has hosted {self.number_served} people.')

    def increment_number_served(self, set):
        self.number_served += set
        print(f'{self.restaurant_name.upper()} has hosted {self.number_served} people as of today.')


# restaurant = Restaurant("Larry's Pizza", 'Pizza')
# ''' creates restaurant class instance '''
# print(restaurant.number_served)
# 
# restaurant.number_served = 12
# '''changes the self.number_served varable'''
# print(restaurant.number_served)
# 
# restaurant.set_number_served(11)
# '''uses the set_number_served method to change the number_served varable'''
# 
# restaurant.increment_number_served(150)
# '''uses the increment_number_served method to change the number_served varable'''


# 9.5

class User:
    '''
    User Class example

    example python Class for a general user in a general system
    '''
    def __init__(self, first_name, last_name, birthday):
        '''initialize attributes to describe any user'''
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{self.first_name.title()} {self.last_name.title()}'
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@example.com'
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self):
        '''return a neatly formated description of a user instance'''
        user_description_message = f'Users current information: \n'
        user_description_message += f'\tUsers name: {self.name}\n'
        user_description_message += f'\tUsers email: {self.email.lower()}\n'
        user_description_message += f'\tUsers birthday: {self.birthday}'
        print(user_description_message)

    def greet_user(self):
        '''returns a simple user instance greatting'''
        greeting = f'Hello {self.name}\n'
        print(greeting)

    def increment_login_attempts(self):
        '''increments the login_attempts varable'''
        self.login_attempts += 1

    def rest_login_attempts(self):
        '''resets the login_attempts varable to 0'''
        self.login_attempts = 0


user1 = User('brian', 'willis', '03-03-1978')
'''creates and instace of the User class'''

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.rest_login_attempts()
print(user1.login_attempts)
