dinner_guests = ['Coby Bryant', 'Micheal Jordon', 'Mark Hamil', 'Harrison Ford']
print(f"{dinner_guests[0]}, your are invited to dinner")
print(f"{dinner_guests[1]}, your are invited to dinner")
print(f"{dinner_guests[2]}, your are invited to dinner")
print(f"{dinner_guests[3]}, your are invited to dinner")

cannot_attend = dinner_guests.pop(0)
print(f"\nUnfortunatly, {cannot_attend} will not be able to join us for dinner.")
dinner_guests.insert(0, 'Carrie Fisher')
print(f"\n{dinner_guests[0]}, your are invited to dinner")
print(f"{dinner_guests[1]}, your are invited to dinner")
print(f"{dinner_guests[2]}, your are invited to dinner")
print(f"{dinner_guests[3]}, your are invited to dinner")
