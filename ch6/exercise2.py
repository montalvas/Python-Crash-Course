people = [
    {
        'name': 'Lucas',
        'age': 27,
        'gender': 'Male',
    },
    {
        'name': 'Miguel',
        'age': 4,
        'gender': 'Male',
    },
    {
        'name': 'Adriana',
        'age': 27,
        'gender': 'Female',
    },
]

for person in people:
    for field, data in person.items():
        print(f"{field.title()}: {data}")
    print("{:=^20}".format(''))