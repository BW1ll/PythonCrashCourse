from user import Admin as A

admin = A('brian', 'willis', '03-03-1978')
admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()