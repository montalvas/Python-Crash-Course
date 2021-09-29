from classes.admin import Admin

super_user = Admin("Miguel", "Albuquerque", "Mikalb")
super_user.greet_user()
super_user.increment_login_attempts()
super_user.describe_user()

super_user.privileges.show_privileges()