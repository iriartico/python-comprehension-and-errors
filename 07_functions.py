def sum(x, y):
    sum = 0
    for i in range(x, y):
        sum += i
    print(sum)


def run():
    sum(1, 10)
    sum(15, 30)


if __name__ == '__main__':
    run()
