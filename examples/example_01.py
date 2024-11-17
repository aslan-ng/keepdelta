import keepdelta as kd


# profile of a person
old = {
    "info": {
        "name": "Alice",
        "age": 30,
        "is_student": True,
        "grades": [85.5, 90.0, 78],
        "preferences": (
            "chocolate", 
            {"sports": {"football", "tennis"}},
        ),
    },
    "meta": {
        "attributes": [
            {"id": 1, "value": "active"},
            {"id": 2, "value": "inactive"}
        ],
        "settings": {
            "dark_mode": True,
            "font_size": 14,
            "scale": 1.25
        }
    }
}

# profile of that person one year later
new = {
    "info": {
        "name": "Alice",
        "age": 31,
        "is_student": False,
        "grades": [85.5, 90.0, 78],
        "preferences": (
            "coffee", 
            {"sports": {"football", "bodybuilding"}},
        ),
    },
    "meta": {
        "attributes": [
            {"id": 1, "value": "inactive"},
            {"id": 2, "value": "inactive"}
        ],
        "settings": {
            "dark_mode": True,
            "font_size": 14,
            "scale": 1.25
        }
    }
}

delta = kd.create(old, new)
print(delta)
var = kd.apply(old, delta)
print(var == new)