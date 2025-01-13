from copy import deepcopy


class DeltaStr:
    """
    Handle deltas for str (string) variables
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
    

if __name__ == '__main__':
    old_var = 'old'
    new_var = 'new'
    expected_delta = 'new'

    # Create delta
    delta = DeltaStr.create(old_var, new_var)
    print('Delta:', delta)
    print('Test delta creation: ', delta == expected_delta)

    # Apply delta
    var = DeltaStr.apply(old_var, delta)
    print('Reconstructed variable:', var)
    print('Test delta application: ', var == new_var)