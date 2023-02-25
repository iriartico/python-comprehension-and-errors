# Example 1
dict = {}
for i in range(1, 11):
    dict[i] = i**2
print(dict)

dict_v2 = {i: i**2 for i in range(1, 11)}
print(dict_v2)


# Example 2
from random import randint

countries = ['col', 'pe', 'bol', 'arg']
population = {}
for country in countries:
    population[country] = randint(1, 100)
print(population)

population_v2 = {country: randint(1, 100) for country in countries}
print(population_v2)


# Example 3
names = ['nico', 'perico', 'santusa']
ages = [12, 56, 34]
print(list(zip(names, ages))) # zip une listas, pero solo regresa la referencia, por eso, es necesario castear con "list"
# Output: [('nico', 12), ('perico', 56), ('santusa', 34)] Retorna una lista con pares de tuplas

people = {name: age for (name, age) in zip(names, ages)}
print(people)
