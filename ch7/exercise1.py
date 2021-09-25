sandwich_orders = ['hamburger', 'pastrami', 'hot dog', 'smash burguer', 'pastrami','beef burguer', 'chiken burguer', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    if sandwich_orders[-1] == 'pastrami':
        print("we are out of pastrami.")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
            
    print(f"The {sandwich_orders[-1]} is finished.")
    finished_sandwiches.append(sandwich_orders.pop())

finished_sandwiches.reverse()

print("The finished sandwiches are: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)