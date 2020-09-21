dinner_guests = ['Coby Bryant', 'Micheal Jordon', 'Mark Hamil', 'Harrison Ford']
# print(f"{dinner_guests[0]}, your are invited to dinner")
# print(f"{dinner_guests[1]}, your are invited to dinner")
# print(f"{dinner_guests[2]}, your are invited to dinner")
# print(f"{dinner_guests[3]}, your are invited to dinner")

cannot_attend = dinner_guests.pop(0)
# print(f"\nUnfortunatly, {cannot_attend} will not be able to join us for dinner.")
dinner_guests.insert(0, 'Carrie Fisher')
# print(f"\n{dinner_guests[0]}, your are invited to dinner")
# print(f"{dinner_guests[1]}, your are invited to dinner")
# print(f"{dinner_guests[2]}, your are invited to dinner")
# print(f"{dinner_guests[3]}, your are invited to dinner")
# print(f'\nI just wanted to let everyone knwo that I was able to get'
#       f' a larger dinner table')

dinner_guests.insert(0, 'Brandon Brulsworth')
dinner_guests.insert(2, 'Jessica Alba')
dinner_guests.append('Frank Jones')

for guest in dinner_guests:
    print(f"Greetings {guest.title()}, your are invited to dinner.")
    print(dinner_guests)
# print(f"{dinner_guests[0]}, your are invited to dinner")
# print(f"{dinner_guests[1]}, your are invited to dinner")
# print(f"{dinner_guests[2]}, your are invited to dinner")
# print(f"{dinner_guests[3]}, your are invited to dinner")
# print(f"{dinner_guests[4]}, your are invited to dinner")
# print(f"{dinner_guests[5]}, your are invited to dinner")
# print(f"{dinner_guests[6]}, your are invited to dinner")

print(f"\nUnfortunatly, my dinner table will not arive in time for dinner, and"
      f" I can only invite two people for dinner")

sorry = dinner_guests.pop(0)
print(f'\nI am sorry {sorry}, I cannot invite you to dinner')
sorry1 = dinner_guests.pop(-1)
print(f'I am sorry {sorry1}, I cannot invite you to dinner')
sorry2 = dinner_guests.pop(-1)
print(f'I am sorry {sorry2}, I cannot invite you to dinner')
sorry3 = dinner_guests.pop(-1)
print(f'I am sorry {sorry3}, I cannot invite you to dinner')
sorry4 = dinner_guests.pop(-1)
print(f'I am sorry {sorry4}, I cannot invite you to dinner')
print(f"\n{dinner_guests[0]}, your are still invited to dinner")
print(f"{dinner_guests[1]}, your are still invited to dinner")

del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)