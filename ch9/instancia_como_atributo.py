from classes.eletric_car_2 import EletricCar

my_tesla = EletricCar('tesla', 'model s', '2021')
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()