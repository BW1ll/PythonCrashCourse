from admin_privileges import Admin, Privileges

admin = Admin('brian', 'willis', '03-03-1978')
admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()