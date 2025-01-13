from keepdelta.types.collections import Delta


def create(old, new):
    return Delta.create(old, new)

def apply(old, delta):
    return Delta.apply(old, delta)


if __name__ == '__main__':
    old = [1, 'hello', {'world': 2}]
    new = [0, 'bye', {'world': 3}]
    delta = create(old, new)
    print('Delta:', delta)
    print('Test is passing:', apply(old, delta) == new)
