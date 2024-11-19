from copy import deepcopy


class DeltaBool:
    """
    Handle deltas for bool variables
    """
    @staticmethod
    def create(old: bool, new: bool):
        """
        Create delta for bool variable
        """
        return deepcopy(new)
    
    @staticmethod
    def apply(old: bool, delta: bool):
        """
        Apply delta to the bool variable
        """
        return deepcopy(delta)
    

if __name__ == "__main__":
    old_var = False
    new_var = True

    delta = DeltaBool.create(old_var, new_var)
    print(delta) # expected: True

    var = DeltaBool.apply(old_var, delta)
    print(var) # expected: True