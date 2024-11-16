from copy import deepcopy

from keepdelta.basic_variables import DeltaBool, DeltaFloat, DeltaInt, DeltaStr


class Delta:
    """
    Handle deltas for all variables
    """

    def create(old, new):
        """
        Create delta by comparing *old* and *new*
        """        
        if type(old) == type(new): # same type
            if old != new: # inequal and same type
                if isinstance(new, bool): # is basic, inequal and same type
                    delta = DeltaBool.create(old, new)
                elif isinstance(new, str):
                    delta = DeltaStr.create(old, new)
                elif isinstance(new, float):
                    delta = DeltaFloat.create(old, new)
                elif isinstance(new, int):
                    delta = DeltaInt.create(old, new)
                elif isinstance(old, dict):
                    delta = DeltaDict.create(old, new)
                elif isinstance(old, list):
                    delta = DeltaList.create(old, new)
                elif isinstance(old, tuple):
                    delta = DeltaList.create(old, new)
                elif old is None:
                    delta = new
                else:
                    print("variable type not recognized: ", type(old))
                    raise ValueError
            else: # equal and same type
                delta = 'NOTHING'
        else: # not same type
            delta = new
        return delta
    
    def apply(old, delta):
        """
        Apply *delta* to *old* variable
        """
        if delta == "NOTHING": # equal and same type
            new = deepcopy(old)
        else:
            if type(old) == type(delta): # same type
                if isinstance(old, bool):
                    new = deepcopy(delta)
                elif isinstance(old, str):
                    new = deepcopy(delta)
                elif isinstance(old, int) or \
                     isinstance(old, float):
                    new = deepcopy(old) + deepcopy(delta)
                elif isinstance(old, dict):
                    new = DeltaDict.apply(old, delta)
                elif isinstance(old, list):
                    new = DeltaList.apply(old, delta)
                elif isinstance(old, tuple):
                    new = DeltaList.apply(old, delta)
                elif old is None:
                    new = deepcopy(delta)
                else:
                    print("variable type not recognized: ", type(old))
                    raise ValueError
            else: # not same type
                new = delta
        return new


class DeltaDict:
    """
    Handle deltas for dictionaries
    """
    def create(old: dict, new: dict) -> dict:
        """
        Create delta by comparing *old* and *new*
        """
        delta = {}
        old_keys = old.keys()
        new_keys = new.keys()
        keys_in_both = list(set(old_keys) & set(new_keys))
        keys_in_old_not_in_new = list(set(old_keys) - set(new_keys))
        keys_in_new_not_in_old = list(set(new_keys) - set(old_keys))
        for key in keys_in_both:
            delta_value = Delta.create(old[key], new[key])
            if delta_value != "NOTHING":
                delta[key] = delta_value
        for key in keys_in_old_not_in_new:
            delta[key] = "DELETE"
        for key in keys_in_new_not_in_old:
            delta_value = Delta.create(None, new[key])
            if delta_value != "NOTHING":
                delta[key] = delta_value
        return delta
    
    def apply(old: dict, delta: dict) -> dict:
        """
        Apply *delta* to *old* dictionary
        """
        new = deepcopy(old)
        for key in delta:
            delta_value = delta[key]
            if key in old:
                if delta_value == "DELETE":
                    del new[key]
                else:
                    new[key] = Delta.apply(old[key], delta_value)
            else:
                new[key] = delta_value
        return new
    

class DeltaList:
    """
    Handle deltas for lists
    """
    def create(old: list, new: list) -> list:
        """
        Create delta by comparing *old* and *new*
        """
        old = DeltaList._list_to_dict(old)
        new = DeltaList._list_to_dict(new)
        return [DeltaDict.create(old, new)]

    def apply(var: list, delta: list) -> list:
        """
        Apply *delta* to *old* list
        """
        var = DeltaList._list_to_dict(var)
        new = DeltaDict.apply(var, delta[0])
        return DeltaList._dict_to_list(new)

    def _list_to_dict(input: list) -> dict:
        """
        Convert list to dictionary
        """
        result = {}
        for i, item in enumerate(input):
            result[i] = item
        return result

    def _dict_to_list(input: dict) -> list:
        """
        Convert dictionary to list
        """
        result = None
        if input is not None:
            result = []
            for i in input:
                if input[i] is not None:
                    result.append(input[i])
        return result


if __name__ == "__main__":
    old = {'a': 1, 'b': 2, 'c': {'d': 5, 'e': 2}}
    new = {'a': 3, 'c': {'d': 5, 'e': 3}}
    expected_delta = {'a': 2, 'b': "DELETE", 'c': {'e': 1}}

    delta = Delta.create(old, new)
    print("creation: ", delta == expected_delta)

    val = Delta.apply(old, delta)
    print("application: ", val == new)
