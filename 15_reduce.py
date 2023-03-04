from functools import reduce


def run():
    numbers = [1, 2, 3, 4, 5]
    result = reduce(lambda counter, item: counter + item, numbers)
    print(result)


if __name__ == '__main__':
    run()
