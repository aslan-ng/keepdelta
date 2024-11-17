from keepdelta.types.collections import Delta


def create(old, new):
    return Delta.create(old, new)


def apply(old, delta):
    return Delta.apply(old, delta)