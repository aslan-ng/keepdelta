from copy import deepcopy


class DeltaComplex:
    """
    Handle deltas for complex variables
    """

    @staticmethod
    def create(old: complex, new: complex) -> complex:
        """
        Create delta for complex variables
        """
        return deepcopy(new) - deepcopy(old)

    @staticmethod
    def apply(old: complex, delta: complex) -> complex:
        """
        Apply delta to the complex variable
        """
        return deepcopy(old) + deepcopy(delta)


if __name__ == "__main__":
    old_var = 2 + 2j
    new_var = 3 + 3j
    expected_delta = 1 + 1j

    # Create delta
    delta = DeltaComplex.create(old_var, new_var)
    print("Delta:", delta)
    print("Test delta creation: ", delta == expected_delta)

    # Apply delta
    var = DeltaComplex.apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
