age = int(input("How old are you? "))
person = ''

if age < 2:
    person = "baby"
elif age < 4:
    person = "child"
elif age < 13:
    person = "kid"
elif age < 20:
    person = "teenager"
elif age < 65:
    person = "adult"
elif age >= 65:
    person = "old man"

print(f"You are a {person}")