users = ['Admin', 'Lucas', 'Adriana', 'Miguel', 'Guest']
logged_users = ['Admin', 'Lucas', 'Guest']

if logged_users:
    for logged_user in logged_users:
        if logged_user == 'Admin':
            print(f"Hi {logged_user}, would you like to see a status report?")
        else:
            print(f"Hi {logged_user}, thanks for log in again")
else:
    print("We need to find some users.")

