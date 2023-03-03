
def run():
    numbers = [1, 2, 3, 4, 32]
    squares = list(map(lambda i: i**2, numbers))
    print('Values: ', numbers)
    print('Squares: ', squares)


if __name__ == '__main__':
    run()
