from random import randint

countries = ['col', 'pe', 'bol', 'arg']

population = {country: randint(1, 100) for country in countries}
print(population)

population_20 = {country: population for (
    country, population) in population.items() if population > 20}
print(population_20)


text = 'Hola, soy Josese'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)
