Simulation has become an indispensable tool in scientific research and discovery. By mimicking real-world processes in a controlled computational environment, simulations enable scientists to explore, predict, and understand complex phenomena that may be difficult, expensive, or impossible to study experimentally.

When running a simulation, there are several approaches to saving results, each with its own pros and cons:
1.	Saving the State at Each Step:
Save the entire state of the simulation at every step.
- Pros: All data is preserved, making it easy to access any point in the simulation.
- Cons: Requires significant storage space, especially for long simulations or large datasets.
2.	Saving the Initial State and Logic:
Save only the initial state (including random seeds), the simulation logic (program or code). Then, the reconstruction of results is done by re-running the simulation from scratch.
- Pros: Requires minimal storage space.
- Cons: Time-consuming to reconstruct results, especially for complex or long-running simulations.
3.	Saving the Initial Values and Deltas Across Steps:
Save the initial state and record only the changes (deltas) at each step. Results can be reconstructed incrementally without re-running the entire simulation.
- Pros: Requires less storage than approach 1, and reconstruction is faster than approach 2.
- Cons: Requires more storage than approach 2 and loading results is slower than approach 1.

Python has emerged as a leading programming language for simulations across various scientific and engineering domains. Its versatility, accessibility, and robust ecosystem make it an essential tool for conducting researches and approach complex real-world questions.

Why KeepDelta is Useful:
KeepDelta is designed for approach 3, offering a balanced solution between storage efficiency and reconstruction speed. It efficiently manages deltas, making it ideal for simulations where both storage and performance are critical. By adopting this method, users can strike the right balance between resource usage and accessibility.


Summary

Managing changes in complex Python data structures during simulations or dynamic data analysis can become resource-intensive, particularly when balancing storage and computational efficiency. KeepDelta is a lightweight Python library that provides tools for creating and applying deltas (differences) between nested Python data structures. It addresses the need for efficient tracking and reconstruction of state changes without requiring the storage of complete snapshots. The library is designed to be human-readable and intuitive, making it suitable for Python-based simulation workflows, data tracking, and similar applications.


Statement of Need

Simulations often require mechanisms to track and store evolving states of data structures across iterations. The naive approach of saving full snapshots is storage-heavy, while recalculating states from scratch can be computationally expensive. KeepDelta introduces a middle ground by saving only the deltas (changes) between states. Unlike existing libraries or binary delta tools like xdelta or bsdiff, KeepDelta is tailored for Python, operating directly on native Python data structures such as dictionaries, lists, tuples, and sets. The results are human-readable and designed for Python developers and researchers who need a simple yet powerful solution for change management.

KeepDelta supports:

Nested and mixed Python data structures.

Compact and efficient delta representation.

Reconstruction of data states by applying deltas.

This library is particularly useful for simulation-based research, iterative computations, and dynamic data updates where minimizing storage and computational overhead is critical.

Features

Delta Creation: Generate compact delta objects that capture changes between two Python data structures.

Delta Application: Apply a delta to an original data structure to recreate the updated version.

Compatibility: Supports all native Python data structures, including:

Primitive types: bool, int, float, str, etc.

Collections: dict, list, tuple, set.

Nested and mixed structures.

Human Readability: Deltas are stored in JSON-like formats, making them easy to understand and debug.

Comparison to Existing Tools

Existing tools such as xdelta, bsdiff, and detools focus on binary data or specific formats, often sacrificing human readability and ease of use in Python environments. KeepDelta is designed specifically for Python developers, ensuring compatibility with Python’s data structures and workflows. Unlike these tools, KeepDelta provides intuitive functions for delta creation and application within Python code, eliminating the need for external utilities or complex integrations.

Usage Example

Delta Creation

import keepdelta as kd

# Initial data
old = {
    "info": {
        "name": "Alice",
        "age": 30,
        "is_student": True,
        "preferences": ("chocolate", {"sports": {"football", "tennis"}}),
    }
}

# Updated data
new = {
    "info": {
        "name": "Alice",
        "age": 31,
        "is_student": False,
        "preferences": ("coffee", {"sports": {"football", "bodybuilding"}}),
    }
}

# Create delta
delta = kd.create(old, new)
print(delta)

Delta Application

# Apply delta
updated = kd.apply(old, delta)
print(updated == new)  # Output: True

Implementation

KeepDelta’s core functionality relies on two primary functions:

create(old, new): Compares two data structures and produces a delta object capturing their differences.

apply(original, delta): Applies the delta to the original data structure to recreate the updated version.

The library efficiently handles deeply nested and mixed structures, ensuring compatibility with various Python workflows.

Current Applications

KeepDelta is ideal for:

Simulations: Efficiently managing state changes across iterations without excessive storage or computation.

Data Versioning: Tracking and reconstructing changes in datasets over time.

Dynamic Applications: Handling frequent updates in nested configurations or settings.




Examples:

https://www.theoj.org/joss-papers/joss.07157/10.21105.joss.07157.pdf
https://github.com/openjournals/joss-reviews/issues/7698
