current_users = ['Miguel', 'Zoro', 'Ikki', 'Shanks', 'Stella']

new_users = ['Ouma', 'Akainu', 'ZORO', 'shANKs', 'Robin']

for new_user in new_users:
    if new_user.capitalize() in current_users:
        print(f"Username {new_user} is not available.")
    else:
        print(f"Username {new_user} is available.")