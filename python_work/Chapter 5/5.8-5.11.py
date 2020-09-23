''' 5.8 Hello Admin '''
print(5.8)
username = ['admin', 'brian', 'sarah', 'erin', 'susan']
for name in username:
    if name == 'admin':
        print(f'Hello {name.title()}, would you like to see a status report?')
    else:
        print(f'Hello {name.title()}, thank your for logging in again')

''' 5.9 No Users '''
print(5.9)
username = []
if username:
    for name in username:
        if name == 'admin':
            print(f'Hello {name.title()}, would you like to see a status report?')
        else:
            print(f'Hello {name.title()}, thank your for logging in again')
else:
    print('We need to get some users!')

''' 5.10 Checking Usernames '''
print(5.10)
current_users = ['brian', 'sarah', 'erin', 'susan', 'noah']
new_users = ['Brian', 'Sarah', 'Geoff', 'Nora', 'Miles']
for new_user in new_users:
    if new_user.lower() in current_users:
            print(f'The username {new_user} is not available.  Please try again.')
    else:
        print(f'Welcome {new_user}.  Thanks for joining!')
        current_users.append(new_user.lower())

print(current_users)

''' 5.11 Ordinal Numbers '''
print(5.11)
nums = [value for value in range(1, 10)]
for num in nums:
    if num != 1 and num != 2 and num != 3:
        print(f'{num}th')
    elif num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')