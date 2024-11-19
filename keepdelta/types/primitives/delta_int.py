from copy import deepcopy


class DeltaInt:
    """
    Handle deltas for int variables
    """
    @staticmethod
    def create(old: int, new: int):
        """
        Create delta for int variable
        """
        return deepcopy(new) - deepcopy(old)
    
    @staticmethod
    def apply(old: int, delta: int):
        """
        Apply delta to the int variable
        """
        return deepcopy(old) + deepcopy(delta)
    

if __name__ == "__main__":
    old_var = 2
    new_var = 3

    delta = DeltaInt.create(old_var, new_var)
    print(delta) # expected: 1

    var = DeltaInt.apply(old_var, delta)
    print(var) # expected: 3