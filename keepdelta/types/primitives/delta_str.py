from copy import deepcopy


class DeltaStr:
    """
    Handle deltas for str variables
    """
    @staticmethod
    def create(old: str, new: str):
        """
        Create delta for str variable
        """
        return deepcopy(new)
    
    @staticmethod
    def apply(old: str, delta: str):
        """
        Apply delta to the str variable
        """
        return deepcopy(delta)
    

if __name__ == "__main__":
    old_var = "old"
    new_var = "new"

    delta = DeltaStr.create(old_var, new_var)
    print(delta) # expected: "new"

    var = DeltaStr.apply(old_var, delta)
    print(var) # expected: "new"