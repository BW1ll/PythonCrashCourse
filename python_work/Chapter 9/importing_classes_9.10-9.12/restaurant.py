'''
A python class for creating a restuarant
'''

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