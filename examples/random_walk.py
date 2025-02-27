"""
The results of Random Walk is saved and loaded using deltas.
"""

import random
from copy import deepcopy

import keepdelta as kd

random.seed(30)  # Set the seed for reproducibility
position = 0  # Initial value
steps = 100

# Save the result by deltas
deltas = []
for _ in range(steps):
    old_position = deepcopy(position)

    # Move one step randomly +1 or -1
    position += random.choice([-1, 1])

    delta = kd.create(old_position, position)
    deltas.append(delta)
print(f">>> Position after {steps} steps: {position}")

# Reconstruct the result
position = 0  # Initial value
for delta in deltas:
    position = kd.apply(position, delta)
print(f">>> Position after loading deltas: {position}")
