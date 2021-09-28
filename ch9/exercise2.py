from classes.user import Users

new_user = Users("lucas", "albuquerque", "montalvas")
new_user.greet_user()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

new_user.describe_user()

new_user.reset_login_attempts()
new_user.describe_user()