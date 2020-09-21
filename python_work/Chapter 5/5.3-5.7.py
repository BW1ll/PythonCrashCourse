
''' 5.3 exersize '''
alien_color = 'green'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.3')
if alien_color == 'yellow':
    print('You shot down a yellow alien and erned 5 points. 5.3')

''' 5.4 exersize '''
alien_color = 'yellow'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.4.1')
elif alien_color == 'yellow':
    print('You shot down a yellow aline and erned 10 points.5.4.1')

alien_color = 'red'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.4.2')
elif alien_color == 'yellow':
    print('You shot down a yellow aline and erned 10 points.5.4.2')

''' 5.5 exersize '''
alien_color = 'red'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.5.1')
elif alien_color == 'yellow':
    print('You shot down a yellow aline and erned 10 points. 5.5.1')
else:
    print('You shot down a red alien and erned 15 points. 5.5.1')

alien_color = 'green'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.5.2')
elif alien_color == 'yellow':
    print('You shot down a yellow aline and erned 10 points. 5.5.2')
else:
    print('You shot down a red alien and erned 15 points. 5.5.2')

alien_color = 'yellow'
if alien_color == 'green':
    print('You shot down a green aline and erned 5 points. 5.5.3')
elif alien_color == 'yellow':
    print('You shot down a yellow aline and erned 10 points. 5.5.3')
else:
    print('You shot down a red alien and erned 15 points. 5.5.3')

''' 5.6 exersize '''
age = 40
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f'This person is a {stage}')

''' 5.7 '''
fruit = ['apple', 'orange', 'banana']
if 'apple' in fruit:
    print('I hate apples!')
if 'orange' in fruit:
    print('I hate oranges!')
if 'banana' in fruit:
    print('I hate bananas!')
if 'crakers' in fruit:
    print('I hate fruit!')
if 'chcolate' in fruit:
    print('I hate fruit!')   