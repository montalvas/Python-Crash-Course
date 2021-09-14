country = ['Canada', 'Australia', 'Alemanha', 'Japao', 'Portugal']
print(country)
print(sorted(country))
print(sorted(country, reverse=True))

#alterando lista permanentemente
country.sort()
print(country)
country.sort(reverse=True)
print(country)