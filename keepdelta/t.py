import keepdelta as kd
old = {
    "name": "Alice",
    "age": 20,
    "is_student": True,
    "grades": [85.5, 90.0, 78],
    "preferences": {
        "drink": "soda",
        "sports": {"football", "tennis"},
    },
}


new = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "grades": [87, 90.0, 78, 92],
    "preferences": {
        "drink": "coffee",
        "sports": {"football", "bodybuilding"},
    },
}

# Create delta
delta = kd.create(old, new)
print(delta)
