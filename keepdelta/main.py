from typing import Union

from keepdelta.types.collections import Delta


def create(
        old: Union[None, bool, complex, float, int, str, dict, list, tuple, set],
        new: Union[None, bool, complex, float, int, str, dict, list, tuple, set],
    ) -> Union[None, bool, complex, float, int, str, dict]:
    """
    Generates a delta representing the differences between the 'old' and 'new' variables.

    Args:
        old (None | bool | complex | float | int | str | dict | list | tuple | set): The original data structure.
        new (None | bool | complex | float | int | str | dict | list | tuple | set): The updated data structure.

    Returns:
        delta (None | bool | complex | float | int | str | dict): A delta object capturing the differences.
    """
    return Delta.create(old, new)

def apply(
        old: Union[None, bool, complex, float, int, str, dict, list, tuple, set],
        delta: Union[None, bool, complex, float, int, str, dict]
    ) -> Union[None, bool, complex, float, int, str, dict, list, tuple, set]:
    """
    Applies a previously generated delta to the 'old' variable to recreate the updated version.

    Args:
        old (None | bool | complex | float | int | str | dict | list | tuple | set): The original data structure.
        delta (None | bool | complex | float | int | str | dict): A delta object to be applied to 'old'.

    Returns:
        new (None | bool | complex | float | int | str | dict | list | tuple | set): The updated data structure.
    """
    return Delta.apply(old, delta)


if __name__ == "__main__":
    old_var = [1, "hello", {"world": 2}]
    new_var = [0, "bye", {"world": 3}]
    expected_delta = {0: -1, 1: 'bye', 2: {'world': 1}}

    # Create delta
    delta = create(old_var, new_var)
    print("Delta:", delta)
    print("Test delta creation: ", delta == expected_delta)

    # Apply delta
    var = apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
