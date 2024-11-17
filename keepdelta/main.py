from keepdelta.delta import Delta


def create(old, new):
    return Delta.create(old, new)


def apply(var, delta):
    return Delta.apply(var, delta)