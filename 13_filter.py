def run():
    numbers = [1, 2, 3, 4, 5]
    pairs = list(filter(lambda x: x % 2 == 0, numbers))
    print(pairs)
    print(numbers)


if __name__ == '__main__':
    run()
