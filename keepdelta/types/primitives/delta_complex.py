from copy import deepcopy


class DeltaComplex:
    """
    Handle deltas for complex variables
    """
    def create(old: complex, new: complex):
        """
        Create delta for complex variable
        """
        return deepcopy(new) - deepcopy(old)
    
    def apply(old: complex, delta: complex):
        """
        Apply delta to the complex variable
        """
        return deepcopy(old) + deepcopy(delta)


if __name__ == "__main__":
    old_var = 2 + 2j
    new_var = 3 + 3j

    delta = DeltaComplex.create(old_var, new_var)
    print(delta) # expected: 1 + 1j

    var = DeltaComplex.apply(old_var, delta)
    print(var) # expected: 3 + 3j