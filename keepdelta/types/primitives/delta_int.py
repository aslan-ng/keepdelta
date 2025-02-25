from copy import deepcopy


class DeltaInt:
    """
    Handle deltas for int (integer) variables
    """

    @staticmethod
    def create(old: int, new: int) -> int:
        """
        Create delta for int variables
        """
        return deepcopy(new) - deepcopy(old)

    @staticmethod
    def apply(old: int, delta: int) -> int:
        """
        Apply delta to the int variable
        """
        return deepcopy(old) + deepcopy(delta)


if __name__ == "__main__":
    old_var = 2
    new_var = 3
    expected_delta = 1

    # Create delta
    delta = DeltaInt.create(old_var, new_var)
    print("Delta:", delta)
    print("Test delta creation: ", delta == expected_delta)

    # Apply delta
    var = DeltaInt.apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
