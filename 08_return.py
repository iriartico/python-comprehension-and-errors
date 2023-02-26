def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, "Hola"


def run():
    volume, a, b = find_volume(width=2)
    print(volume, b)


if __name__ == '__main__':
    run()
