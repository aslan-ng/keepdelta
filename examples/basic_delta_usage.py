"""
In this example, we will use dictionaries to demonstrate the basic usage of KeepDelta.
"""

import keepdelta as kd

# State of a smart home
home_state = {
    "owner": "Alice",  # string
    "temperature": {  # dictionary of numbers
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 73.9,
    },
    "lights": {  # dictionary of booleans
        "living_room": True,  # on
        "kitchen": False,  # off
        "bedroom": False,  # off
    },
    "door_lock": False,  # boolean, False means unlocked
    "schedule": ("07:00 wake-up", "22:00 bedtime"),  # tuple of strings
    "alerts": None  # set of strings, currently no alerts
}

# Profile of that person five years later
home_state_new = {
    "owner": "Alice",
    "temperature": {
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 72.7,  # changed from 73.9 → 72.7
    },
    "lights": {
        "living_room": False,  # changed from False (off) → True (on)
        "kitchen": False,
        "bedroom": False,
    },
    "door_lock": True,  # changed from False (Unlocked) → True (Locked)
    "schedule": ("07:00 wake-up", "22:00 bedtime"),
    "alerts": {"low-battery"}  # changed from None to {"low-battery"}
}

# Create delta
delta = kd.create(home_state, home_state_new)
print("Delta:\n", delta)

# Apply delta
home_state_reconstructed = kd.apply(home_state, delta)
print("\nReconstruction is successful:", home_state_reconstructed == home_state_new)
