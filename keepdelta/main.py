from keepdelta.types.collections import Delta


def create(old, new):
    """
    Generates a delta representing the differences between the 'old' and 'new' variables.

    Parameters:
    - old: The original data structure, restricted to supported types.
    - new: The updated data structure of the same type as 'old'.

    Returns:
    - A delta object capturing the differences between 'old' and 'new'.
    """
    return Delta.create(old, new)


def apply(old, delta):
    """
    Applies a previously generated delta to the 'old' variable to recreate the updated version.

    Parameters:
    - old: The original data structure, restricted to supported types.
    - delta: A delta object capturing the differences to be applied to 'old'.

    Returns:
    - The updated data structure after applying the delta.
    """
    return Delta.apply(old, delta)


if __name__ == "__main__":
    old_var = [1, "hello", {"world": 2}]
    new_var = [0, "bye", {"world": 3}]
    expected_delta = create(old_var, new_var)

    # Create delta
    delta = Delta.create(old_var, new_var)
    print("Delta:", delta)
    print("Test delta creation: ", delta == expected_delta)

    # Apply delta
    var = Delta.apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
