'''
Python module of classes for making users
'''

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