from classes.user import User

new_user = User("lucas", "albuquerque", "montalvas")
new_user.greet_user()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

new_user.describe_user()

new_user.reset_login_attempts()
new_user.describe_user()