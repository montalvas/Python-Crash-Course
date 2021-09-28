from classes.dog import Dog

#instanciando uma classe
my_dog = Dog("Trovao", 4)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_back()
print()

your_dog = Dog("doguinho", 400)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_back()