def increment(x):
    return x + 1


def run():
    increment_v2 = lambda x : x + 1
    result = increment(5)
    result2 = increment_v2(20)
    full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
    text = full_name('jose', 'iriarte')

    print(result, result2)
    print(text)


if __name__ == '__main__':
    run()
