from copy import deepcopy

from keepdelta.types.primitives import DeltaBool, DeltaComplex, DeltaFloat, DeltaInt, DeltaStr
from keepdelta.config import keys


class Delta:
    """
    Handle deltas for all variables
    """
    @staticmethod
    def create(old, new):
        """
        Create delta for the variable
        """
        if type(old) == type(new): # same type
            if old != new: # inequal and same type
                if old is None: # none
                    delta = new
                elif isinstance(new, bool): # bool
                    delta = DeltaBool.create(old, new)
                elif isinstance(new, complex): # complex
                    delta = DeltaComplex.create(old, new)
                elif isinstance(new, str): # str
                    if new in keys: 
                        print("variables simialar to keys are not possible to digest: ", new)
                        raise ValueError
                    elif old in keys:
                        print("variables simialar to keys are not possible to digest: ", old)
                        raise ValueError
                    else:
                        delta = DeltaStr.create(old, new)
                elif isinstance(new, float): # float
                    delta = DeltaFloat.create(old, new)
                elif isinstance(new, int): # int
                    delta = DeltaInt.create(old, new)
                elif isinstance(old, dict): # dict
                    delta = DeltaDict.create(old, new)
                elif isinstance(old, list): # list
                    delta = DeltaList.create(old, new)
                elif isinstance(old, tuple): # tuple
                    delta = DeltaTuple.create(old, new)
                elif isinstance(old, set): # set
                    delta = DeltaSet.create(old, new)
                else:
                    print("variable type not supported: ", type(old))
                    raise ValueError
            else: # equal and same type
                delta = keys['nothing']
        else: # not same type
            delta = new # rewrite type
        return delta
    
    @staticmethod
    def apply(old, delta):
        """
        Apply delta to the variable
        """
        if delta == keys['nothing']: # equal and same type
            new = deepcopy(old)
        else:
            if old is None: # none
                new = deepcopy(delta)
            elif isinstance(old, bool): # bool
                new = DeltaBool.apply(old, delta)
            elif isinstance(old, complex): # complex
                new = DeltaComplex.apply(old, delta)
            elif isinstance(old, str): # str
                new = DeltaStr.apply(old, delta)
            elif isinstance(old, float): # float
                new = DeltaFloat.apply(old, delta)
            elif isinstance(old, int): # int
                new = DeltaInt.apply(old, delta)
            elif isinstance(old, dict): # dict
                new = DeltaDict.apply(old, delta)
            elif isinstance(old, list): # list
                new = DeltaList.apply(old, delta)
            elif isinstance(old, tuple): # tuple
                new = DeltaTuple.apply(old, delta)
            elif isinstance(old, set): # set
                new = DeltaSet.apply(old, delta)
            else: # variable type not recognized
                new = deepcopy(delta)
        return new


class DeltaDict:
    """
    Handle deltas for dict variables
    """
    @staticmethod
    def create(old: dict, new: dict) -> dict:
        """
        Create delta for dict variable
        """
        delta = {}
        old_keys = old.keys()
        new_keys = new.keys()
        keys_in_both = list(set(old_keys) & set(new_keys))
        keys_in_old_not_in_new = list(set(old_keys) - set(new_keys))
        keys_in_new_not_in_old = list(set(new_keys) - set(old_keys))
        for key in keys_in_both:
            delta_value = Delta.create(old[key], new[key])
            if delta_value != keys['nothing']:
                delta[key] = delta_value
        for key in keys_in_old_not_in_new:
            delta[key] = keys['delete']
        for key in keys_in_new_not_in_old:
            delta_value = Delta.create(None, new[key])
            if delta_value != keys['nothing']:
                delta[key] = delta_value
        return delta
    
    @staticmethod
    def apply(old: dict, delta: dict) -> dict:
        """
        Apply delta to the dict variable
        """
        new = deepcopy(old)
        for key in delta:
            delta_value = delta[key]
            if key in old:
                if delta_value == keys['delete']:
                    del new[key]
                else:
                    new[key] = Delta.apply(old[key], delta_value)
            else:
                new[key] = delta_value
        return new
    

class DeltaList:
    """
    Handle deltas for list variables
    """
    @staticmethod
    def create(old: list, new: list) -> dict:
        """
        Create delta for list variable
        """
        old = DeltaList._list_to_dict(old)
        new = DeltaList._list_to_dict(new)
        return DeltaDict.create(old, new)

    @staticmethod
    def apply(old: list, delta: dict) -> list:
        """
        Apply delta to the list variable
        """
        old_dict = DeltaList._list_to_dict(old)
        new_dict = DeltaDict.apply(old_dict, delta)
        return DeltaList._dict_to_list(new_dict)

    @staticmethod
    def _list_to_dict(input: list) -> dict:
        """
        Convert list to dictionary
        """
        result = {}
        for i, item in enumerate(input):
            result[i] = item
        return result

    @staticmethod
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
    

class DeltaTuple:
    """
    Handle deltas for tuple variables
    """
    @staticmethod
    def create(old: tuple, new: tuple) -> dict:
        """
        Create delta for tuple variable
        """
        old_list = list(old)
        new_list = list(new)
        return DeltaList.create(old_list, new_list)

    @staticmethod
    def apply(old: tuple, delta: dict) -> tuple:
        """
        Apply delta to the tuple variable
        """
        old_list = list(old)
        new_list = DeltaList.apply(old_list, delta)
        return tuple(new_list)
    

class DeltaSet:
    """
    Handle deltas for set variables
    """
    @staticmethod
    def create(old: set, new: set) -> dict:
        """
        Create delta for set variable
        """
        delta = {}
        # Add annotation
        annotated_old = DeltaSet.add_annotation(old)
        annotated_new = DeltaSet.add_annotation(new)
        # Elements to add
        elements_to_add = annotated_new - annotated_old
        if len(elements_to_add) > 0:
            elements_to_add = DeltaSet.remove_annotation(elements_to_add)
            delta[keys['add to set']] = elements_to_add
        # Elements to remove
        elements_to_remove = annotated_old - annotated_new
        if len(elements_to_remove) > 0:
            elements_to_remove = DeltaSet.remove_annotation(elements_to_remove)
            delta[keys['remove from set']] = elements_to_remove
        return delta
    
    @staticmethod
    def apply(old: set, delta: dict) -> set:
        """
        Apply delta to the set variable
        """
        # Distinguish between bool and other types
        old_bools = {x for x in old if isinstance(x, bool)}
        add_bools = {x for x in delta.get(keys['add to set'], set()) if isinstance(x, bool)}
        remove_bools = {x for x in delta.get(keys['remove from set'], set()) if isinstance(x, bool)}
        old_non_bools = old - old_bools
        add_non_bools = delta.get(keys['add to set'], set()) - add_bools
        remove_non_bools = delta.get(keys['remove from set'], set()) - remove_bools
        updated_non_bools = (old_non_bools | add_non_bools) - remove_non_bools
        updated_bools = (old_bools | add_bools) - remove_bools
        return updated_non_bools | updated_bools

    @staticmethod
    def add_annotation(var: set) -> set:
        """
        Add type of each variable
        """
        return {(x, str(type(x))) for x in var}
    
    @staticmethod
    def remove_annotation(var: set) -> set:
        """
        Remove type of each variable
        """
        return {x[0] for x in var}


if __name__ == "__main__":
    old = {'a': 1, 'b': 2, 'c': {'d': 5, 'e': 2}}
    new = {'a': 3, 'c': {'d': 5, 'e': 3}}
    expected_delta = {'a': 2, 'b': "D3L373", 'c': {'e': 1}}

    delta = Delta.create(old, new)
    #print(delta)
    print("create: ", delta == expected_delta)

    var = Delta.apply(old, delta)
    #print(var)
    print("apply: ", var == new)
