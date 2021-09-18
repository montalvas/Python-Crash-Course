age_0 = 22
age_1 = 33

if (age_0 >= 21) and (age_1 >= 21):
    print('Ok')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['Joe', 'Margaret', 'Rogan']
user = 'Marie'
if user not in banned_users:
    print(f'{user.capitalize()}, you can post a response if you wish')

age = 27
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
#melhorando código
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is ${:.2f}.".format(price))