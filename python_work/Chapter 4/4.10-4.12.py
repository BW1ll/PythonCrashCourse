'''4.10 exersizes'''
names = ['Brandon Brulsworth', 'Carrie Fisher', 'Jessica Alba', 'Micheal Jordon',
         'Mark Hamil', 'Harrison Ford', 'Frank Jones']

print("The first three items in the last are: ")
for name in names[:3]:
    print(name.title())
    
print("\nThese are the items from the middle of the list")
for name in names[2:5]:
    print(name.title())

print("\nThe last thre items in the list are:")
for name in names[-3:]:
    print(name.title())

'''4.11 exersizes'''
my_pizza = ['peperoni', 'sausge', 'bacon']
friends_pizza = my_pizza[:]
my_pizza.append('meat')
friends_pizza.append('cheese')

print("\nMy faviorit pizzas are:")
print(my_pizza)

print("\nMy friedns favorit pizzas are:")
print(friends_pizza)

'''4.11 exersizes'''
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for pizza in my_pizza:
    print(pizza)

print("\nMy friend's favorite foods are:")
for pizza in friends_pizza:
    print(pizza)
