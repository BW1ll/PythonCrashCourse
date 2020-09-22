'''
Python module of class for making admin users
'''

from user2 import User

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

class Admin(User):
    '''special user Admin that inherits from User class'''

    def __init__(self, first_name, last_name, birthday):
        super().__init__(first_name, last_name, birthday)
        self.privileges = Privileges()