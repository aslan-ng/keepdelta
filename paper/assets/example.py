import keepdelta as kd

# (a) previous state
home_state = {
    "owner": "Alice",
    "temperature": {
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 73.9,
    },
    "lights": {
        "living_room": True,
        "kitchen": False,
        "bedroom": False,
    },
    "door_lock": False,
    "schedule": ("07:00 wake-up", "12:00 lunch"),
    "alerts": None
}

# (b) updated state
home_state_new = {
    "owner": "Alice",
    "temperature": {
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 72.7,
    },
    "lights": {
        "living_room": False,
        "kitchen": False,
        "bedroom": False,
    },
    "door_lock": True,
    "schedule": ("07:00 wake-up", "12:00 lunch", "22:00 bedtime"),
    "alerts": {"low-battery"}
}

# (c) delta
delta = kd.create(home_state, home_state_new)
print(delta)


"""
To generate view:
"""

# (a) previous state

{
    "owner": "Alice",
    "temperature": {
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 73.9,
    },
    "lights": {
        "living_room": True,
        "kitchen": False,
        "bedroom": False,
    },
    "door_lock": False,
    "schedule": (
        "07:00 wake-up",
        "12:00 lunch"
    ),
    "alerts": None
}

# (b) updated state

{
    "owner": "Alice",
    "temperature": {
        "living_room": 70.5,
        "kitchen": 71.2,
        "bedroom": 72.7,
    },
    "lights": {
        "living_room": False,
        "kitchen": False,
        "bedroom": False,
    },
    "door_lock": True,
    "schedule": (
        "07:00 wake-up",
        "12:00 lunch",
        "22:00 bedtime"
    ),
    "alerts": {"low-battery"}
}

# (c) delta

{
    "temperature": {
        "bedroom": -1.2
    },
    "lights": {
        "living_room": False
    },
    "door_lock": True,
    "schedule": {
        2: "22:00 bedtime"
    },
    "alerts": {"low-battery"},
}
