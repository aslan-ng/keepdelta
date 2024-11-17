# KeepDelta
Efficient Delta Management for Python Data Structures

A lightweight Python library for creating and applying deltas (differences) between two native Python data structures. This is useful for tracking changes in nested data structures such as dictionaries, lists, tuples, sets, and more.

## Features
* Generate compact delta objects that describe differences between two Python data structures.
* Apply a delta to an original data structure to reconstruct the updated version.
* Supports native Python data structures: dict, list, tuple, set, int, float, bool, str, and more.
* Handles deeply nested and mixed data structures efficiently.

## Installation
Install the package using pip:
```sh
pip install keepdelta
```

## Usage
1. Create Delta
The *create* function generates a delta object that captures the differences between two data structures.

Example:
```
import keepdelta as kd

# Initial data
old = {
    "info": {
        "name": "Alice",
        "age": 30,
        "is_student": True,
        "preferences": (
            "chocolate", 
            {"sports": {"football", "tennis"}},
        ),
    }
}

# Updated data
new = {
    "info": {
        "name": "Alice",
        "age": 31,
        "is_student": False,
        "preferences": (
            "coffee", 
            {"sports": {"football", "bodybuilding"}},
        ),
    }
}

# Create delta
delta = kd.create(old, new)
print(delta)
```

Output:
```
{
    "info": {
        "is_student": False,
        "age": 1,
        "preferences": {
            0: "coffee",
            1: {"sports": {0:"football", 1: "bodybuilding"}}
        }
    }
}
```

2. Apply Delta
The *apply* function takes an original data structure and a delta, then applies the delta to recreate the updated structure.

Example:
```python
# Apply delta
updated = kd.apply(old, delta)

# Verify the update
print(updated == new)  # Output: True
```

## How It Work
1.	create(old, new):
* Compares the old and new data structures.
* Produces a compact delta object containing only the differences.
2.	apply(original, delta):
* Applies the delta to the original data structure.
* Produces the new data structure.

## Contributing
Contributions are welcome! Feel free to:
* Report issues.
* Submit feature requests.
* Create pull requests.

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.