numbers = []

for element in range(1, 11):
    numbers.append(element)
print(numbers)

numbers_v2 = [element for element in range(1, 11) if element % 2 != 0]
print(numbers_v2)
