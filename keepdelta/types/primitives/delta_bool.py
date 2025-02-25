from copy import deepcopy


class DeltaBool:
    """
    Handle deltas for bool (boolean) variables
    """

    @staticmethod
    def create(old: bool, new: bool) -> bool:
        """
        Create delta for bool variables
        """
        return deepcopy(new)

    @staticmethod
    def apply(old: bool, delta: bool) -> bool:
        """
        Apply delta to the bool variable
        """
        return deepcopy(delta)


if __name__ == "__main__":
    old_var = False
    new_var = True
    expected_delta = True

    # Create delta
    delta = DeltaBool.create(old_var, new_var)
    print("Delta:", delta)
    print("Test delta creation: ", delta == expected_delta)

    # Apply delta
    var = DeltaBool.apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
