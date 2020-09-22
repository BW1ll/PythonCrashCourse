'''
Python Crash Course - chapter 9  - Classes

Try it your self exercises
'''

# 9.6


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
        print(
            f'{self.restaurant_name.upper()} has hosted {self.number_served} people as of today.')


class IceCreamStand(Restaurant):
    '''represents a specific typ of restaurant in the Restaurant Class'''

    def __init__(self, restaurant_name, cuisine_type='Ice Cream Stand'):
        '''Initialize attributes of the parent class.'''
        super().__init__(restaurant_name, cuisine_type='Ice Cream Stand')
        self.cuisine_type = 'Ice Cream Stand'
        self.flavors = ['vanila', 'chocolate', 'rocky road',
                        'mint chocolate chip', 'chocolate chip cookie dough']

    def show_flavors(self):
        '''method to list flavors'''
        message = f'We have the following flavors: \n'
        for flavor in self.flavors:
            message += f'\t{flavor}\n'
        print(message)


# scoop_dog = IceCreamStand('scoop dog')
# scoop_dog.show_flavors()

# 9.7


#class User:
#    '''
#    User Class example
#
#    example python Class for a general user in a general system
#    '''
#
#    def __init__(self, first_name, last_name, birthday):
#        '''initialize attributes to describe any user'''
#        self.first_name = first_name
#        self.last_name = last_name
#        self.name = f'{self.first_name.title()} {self.last_name.title()}'
#        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@example.com'
#        self.birthday = birthday
#        self.login_attempts = 0
#
#    def describe_user(self):
#        '''return a neatly formated description of a user instance'''
#        user_description_message = f'Users current information: \n'
#        user_description_message += f'\tUsers name: {self.name}\n'
#        user_description_message += f'\tUsers email: {self.email.lower()}\n'
#        user_description_message += f'\tUsers birthday: {self.birthday}'
#        print(user_description_message)
#
#    def greet_user(self):
#        '''returns a simple user instance greatting'''
#        greeting = f'Hello {self.name}\n'
#        print(greeting)
#
#    def increment_login_attempts(self):
#        '''increments the login_attempts varable'''
#        self.login_attempts += 1
#
#    def rest_login_attempts(self):
#        '''resets the login_attempts varable to 0'''
#        self.login_attempts = 0


# class Admin(User):
#     '''special user Admin that inherits from User class'''
# 
#     def __init__(self, first_name, last_name, birthday):
#         super().__init__(first_name, last_name, birthday)
#         self.privileges = ['add post', 'delete post', 'pin post',
#                            'ban user', 'modify user', 'mange privileged users']
# 
#     def show_privileges(self):
#         message = f'Admin user {self.name.title()} can perform the following tasks: \n'
#         for item in self.privileges:
#             message += f'\t{item}\n'
#         print(message)

# admin1 = Admin('brian', 'willis', '03-03-1978')
# admin1.show_privileges()

# 9.8


class Privileges:
    '''special user Admin that inherits from User class'''

    def __init__(self):
        self.privileges = ['add post', 'delete post', 'pin post',
                           'ban user', 'modify user', 'mange privileged users']

    def show_privileges(self):
        message = f'Admin user can perform the following tasks: \n'
        for item in self.privileges:
            message += f'\t{item}\n'
        print(message)

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


class Admin(User):
    '''special user Admin that inherits from User class'''

    def __init__(self, first_name, last_name, birthday):
        super().__init__(first_name, last_name, birthday)
        self.privileges = Privileges()


admin2 = Admin('brian', 'willis', '03-03-1978')

admin2.privileges.show_privileges()