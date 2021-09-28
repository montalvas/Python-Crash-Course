from classes.restaurant import Restaurant

adriana_restaurant = Restaurant("Bistro da Dri", "Comida classica")
adriana_restaurant.describe_restaurant()
adriana_restaurant.open_restaurant()
adriana_restaurant.set_number_served(10)
adriana_restaurant.get_number_served()
adriana_restaurant.increment_number_served(10)
adriana_restaurant.get_number_served()

my_restaurant = Restaurant("Suculento Burguer", "Hamburgueria")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(30)
my_restaurant.get_number_served()
my_restaurant.increment_number_served(15)
my_restaurant.get_number_served()