from keepdelta.types.collections import Delta


def create(old, new):
    return Delta.create(old, new)

def apply(old, delta):
    return Delta.apply(old, delta)


if __name__ == '__main__':
    old_var = [1, 'hello', {'world': 2}]
    new_var = [0, 'bye', {'world': 3}]
    expected_delta = create(old_var, new_var)

    # Create delta
    delta = Delta.create(old_var, new_var)
    print('Delta:', delta)
    print('Test delta creation: ', delta == expected_delta)

    # Apply delta
    var = Delta.apply(old_var, delta)
    print('Reconstructed variable:', var)
    print('Test delta application: ', var == new_var)
