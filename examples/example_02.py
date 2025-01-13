import keepdelta as kd

# Initial data
old = {
    'info': {
        'name': 'Alice',
        'age': 30,
        'is_student': True,
        'preferences': (
            'chocolate', 
            {'sports': {'football', 'tennis'}},
        ),
    }
}

# Updated data
new = {
    'info': {
        'name': 'Alice',
        'age': 31,
        'is_student': False,
        'preferences': (
            'coffee', 
            {'sports': {'football', 'bodybuilding'}},
        ),
    }
}

# Create delta
delta = kd.create(old, new)
print('Delta:', delta)

# Apply delta
var = kd.apply(old, delta)
print('Test is passing:', var == new)