from copy import deepcopy


class DeltaFloat:
    """
    Handle deltas for float variables
    """

    @staticmethod
    def create(old: float, new: float) -> float:
        """
        Create delta for float variables
        """
        return deepcopy(new) - deepcopy(old)

    @staticmethod
    def apply(old: float, delta: float) -> float:
        """
        Apply delta to the float variable
        """
        return deepcopy(old) + deepcopy(delta)


if __name__ == "__main__":
    old_var = 1.3
    new_var = 3.7
    expected_delta = 2.4

    # Create delta
    delta = DeltaFloat.create(old_var, new_var)
    print("Delta:", delta)
    tolerance = 1e-9
    print("Test delta creation: ", abs(delta - expected_delta) <= tolerance)

    # Apply delta
    var = DeltaFloat.apply(old_var, delta)
    print("Reconstructed variable:", var)
    print("Test delta application: ", var == new_var)
