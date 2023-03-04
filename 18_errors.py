def run():
    try:
        print(0/0)
        assert 1 != 1, 'Uno no es igual que uno'
    except ZeroDivisionError as error:
        print(error)
    except AssertionError as error:
        print(error)

    print('Hola')


if __name__ == '__main__':
    run()
