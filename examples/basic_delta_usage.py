"""
In this example, we will use dictionaries to demonstrate the basic usage of KeepDelta.
"""

import keepdelta as kd

# Profile of a person
profile = {
    "name": "Alice",
    "age": 20,
    "is_student": True,
    "grades": [85.5, 90.0, 78],
    "preferences": {
        "drink": "soda",
        "sports": {"football", "tennis"},
    },
}

# Profile of that person five years later
profile_new = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "grades": [85.5, 90.0, 78, 92],
    "preferences": {
        "drink": "coffee",
        "sports": {"football", "bodybuilding"},
    },
}

# Create delta
delta = kd.create(profile, profile_new)
print("Delta:\n", delta)

# Apply delta
profile_reconstructed = kd.apply(profile, delta)
print("\nReconstruction is successful:", profile_reconstructed == profile_new)
