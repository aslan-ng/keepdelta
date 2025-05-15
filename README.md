<h1 align="center">
    <br>
    <img src="https://raw.githubusercontent.com/aslan-ng/keepdelta/refs/heads/main/assets/logo.png" alt="KeepDelta" width="120">
    <br>
    KeepDelta
</h1>

<h3 align="center">
    Efficient Data Differencing for Python Data Structures
</h3>

<div align="center">

![Python Version](https://img.shields.io/badge/python-≥3.7-blue)
[![PyPI Version](https://img.shields.io/pypi/v/keepdelta.svg)](https://pypi.org/project/keepdelta/)
[![GitHub](https://img.shields.io/badge/github-30363f?logo=github&logoColor=white)](https://github.com/aslan-ng/keepdelta)
[![Coverage Status](https://coveralls.io/repos/github/aslan-ng/keepdelta/badge.svg?branch=main)](https://coveralls.io/github/aslan-ng/keepdelta?branch=main)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br/>
[![status](https://joss.theoj.org/papers/fe9cc7429528b344b4b6561fdf674f45/status.svg)](https://joss.theoj.org/papers/fe9cc7429528b344b4b6561fdf674f45)

</div>

![Header Image](https://raw.githubusercontent.com/aslan-ng/keepdelta/refs/heads/main/assets/header.png)

*KeepDelta* is a lightweight Python library designed to efficiently track and manage changes (deltas) between Python built-in types. It is applicable to various scenarios  that require dynamic data management, especially when incremental numerical changes are present, such as simulations and sensing. While many alternative tools operate at the binary level, KeepDelta emphasizes human-readable delta encoding, facilitating debugging and analysis for Python developers and researchers across multiple domains.

## What is Delta Encoding?

In many computational scenarios, efficiently managing evolving data is crucial. Traditional methods, that rely on full-state encoding — which means storing and/or transmitting complete snapshots at each step — can be inefficient due to the large size of the snapshots. Delta encoding addresses this challenge by capturing and applying only the changes (deltas) between successive states of data structures, resulting in significantly smaller and more manageable data.

<div align="center">
    <img src="https://raw.githubusercontent.com/aslan-ng/keepdelta/refs/heads/main/assets/delta_encoding.png" alt="Comparison between traditional data management method and delta encoding." width="500">
    </br>
    <blockquote>
        <em>
        Managing evolving data structures: full-state encoding (left) stores the entire system state at each timestep, represented by colored blocks. In contrast, delta encoding (right) records only the differences between states, highlighted by colored arrows and identified by Δ, providing a more efficient solution for storage and/or transmission.
        </em>
    </blockquote>
</div>

## Features

* Generates compact and human-readable differences between two Python variables.
* Applies delta to a variable to reconstruct the updated version.
* Supports common Python built-in data types.
* Handles deeply nested and mixed data structures efficiently.
* Requires no external dependencies.

## Installation

Install the package using pip:
```sh
pip install keepdelta
```

## Usage

There are two core methods corresponding to the creation and application of delta encodings:

### 1. `create(old, new)`:

The `create` function compares the `old` and `new` variables to generate `delta` that captures the differences between two data structures. It produces a compact data structure containing only these differences, and its high human readability greatly aids debugging during development.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = {
...     "name": "Alice",
...     "age": 20,
...     "is_student": True
... }

>>> # Updated data
>>> new = {
...     "name": "Alice",
...     "age": 25,
...     "is_student": False
... }

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    "age": 5,
    "is_student": False
}
```

### 2. `apply(old, delta)`:

The `apply` function takes the `old` variable and the `delta`, then applies the `delta` to recreate the updated, `new` variable.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = {
...     "name": "Alice",
...     "age": 20,
...     "is_student": True
... }

>>> # Delta
>>> delta = {
...     "age": 5,
...     "is_student": False
... }

>>> # Apply delta
>>> new = kd.apply(old, delta)
>>> print(new)
{
    "name": "Alice",
    "age": 25,
    "is_student": False
}
```

For more usage examples, refer to the [`examples`](https://github.com/aslan-ng/KeepDelta/tree/main/examples) folder in the project repository, or continue to the next section, "[Supported Data Types & Behaviors](#supported-data-types--behaviors)”, for a detailed look at how each structure is handled.

## Supported Data Types & Behaviors

KeepDelta supports common native Python data structures, ensuring compatibility and flexibility when working with a wide variety of data types. The currently supported structures are listed below. Click any item to see how it’s handled and view a quick example:

### 🔸 Primitive Types:

<details>
<summary>
    <b>Boolean</b> (<code>bool</code>)
</summary>
<br>

Since booleans have only two states, the delta is simply the new state (True or False).

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = False

>>> # Updated data
>>> new = True

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
True
```
<br>
</details>

<details>
<summary>
    <b>String</b> (<code>str</code>)
</summary>
<br>

The delta for strings is simply the new string value.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = "hello"

>>> # Updated data
>>> new = "bye"

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
bye
```
<br>
</details>

<details>
<summary>
    <b>Integer</b> (<code>int</code>)
</summary>
<br>

For integers, the delta is computed as subtraction of values, yielding the offset to apply during reconstruction.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = 42

>>> # Updated data
>>> new = 45

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
3
```
<br>
</details>

<details>
<summary>
    <b>Float</b> (<code>float</code>)
</summary>
<br>

For floats, the delta is computed as subtraction of values, yielding the offset to apply during reconstruction.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = 3.13

>>> # Updated data
>>> new = 3.14

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
0.01
```
<br>
</details>

<details>
<summary>
    <b>Complex</b> (<code>complex</code>)
</summary>
<br>

For complex numbers, the delta is computed as subtraction of values, yielding the offset to apply during reconstruction.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = 3+4j

>>> # Updated data
>>> new = 1+5j

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
(-2+1j)
```
<br>
</details>

<details>
<summary>
    <b>NoneType</b> (<code>None</code>)
</summary>
<br>

Since KeepDelta supports type change, it is possible to track the changes from `None` to other types or vise versa.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = 1.62

>>> # Updated data
>>> new = None

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
None
```
<br>
</details>

### 🔸 Collections:

<details>
<summary>
    <b>Dictionary</b> (<code>dict</code>)
</summary>
<br>

When diffing dictionaries, key-value pairs in the inputs are compared. The key removal is marked with the special token `__delete__`.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = {
...     "location": "earth",
...     "age": 20,
...     "snacks": ["chocolate", "bananas"],
...     "student": True,
... }

>>> # Updated data
>>> new = {
...     "location": "mars",
...     "age": 30,
...     "snacks": ["chocolate", "bananas"],
...     "happy": True,
... }

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    "location": "mars",  # Location changed from "earth" → "mars"
    "age": 10,  # Age increased by 10
    "student": "__delete__",  # The removed key
    "happy": True  # The newly added key
}
```
<br>
</details>

<details>
<summary>
    <b>List</b> (<code>list</code>)
</summary>
<br>

The delta for a list is a dictionary where each key is a list index and each value describes the change applied at that position; including a numerical offset (to adjust the original element) or `__delete__` (to remove it).

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = [2, 3, 5, 7]

>>> # Updated data
>>> new = [2, 3, 4]

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    2: -1,  # Third element has been decreased by 1
    3: "__delete__"  # Fourth element has been deleted
}
```
<br>
</details>

<details>
<summary>
    <b>Tuple</b> (<code>tuple</code>)
</summary>
<br>

The delta for a tuple is a dictionary where each key is a list index and each value describes the change applied at that position; including a numerical offset (to adjust the original element) or `__delete__` (to remove it).

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = (2, 3, 5, 7)

>>> # Updated data
>>> new = (2, 3, 4)

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    2: -1,  # Third element has been decreased by 1
    3: "__delete__"  # Fourth element has been deleted
}
```
<br>
</details>

<details>
<summary>
    <b>Set</b> (<code>set</code>)
</summary>
<br>

For sets, the delta is a dict with two special keys: `__add__` for items to add and `__remove__` for items to drop.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = {1, 2, 3}

>>> # Updated data
>>> new = {2, 3, 5, 7}

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    "__add__": {5, 7},  # Numbers added
    "__remove__": {1}  # Numbers removed
}
```
<br>
</details>

<details>
<summary>
    <b>Nested & Composite Structures</b>
</summary>
<br>

KeepDelta supports deeply nested combinations of variables, enabling structures like dictionaries of dictionaries, lists of sets, and other complex, interwoven data types.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = {
...     "name": "Alice",
...     "age": 20,
...     "is_student": True,
...     "grades": [85.5, 90.0, 78],
...     "preferences": {
...         "drink": "soda",
...         "sports": {"football", "tennis"},
...     },
... }

>>> # Updated data
>>> new = {
...     "name": "Alice",
...     "age": 25,
...     "is_student": False,
...     "grades": [87, 90.0, 78, 92],
...     "preferences": {
...         "drink": "coffee",
...         "sports": {"football", "bodybuilding"},
...     },
... }

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
{
    "is_student": False,  # Changed from True → False
    "grades": {
        0: 87,  # Updated from 85.5 → 87
        3: 92  # New grade appended
    },
    "preferences": {
        "drink": "coffee",  # Switched from “soda” → "coffee"
        "sports": {
            "__add__": {"bodybuilding"},  # Sport added
            "__remove__": {"tennis"}  # Sport removed
        }
    },
    "age": 5  # Increased by 5
}
```
<br>
</details>

### 🔸 Special Cases:

<details>
<summary>
    <b>Type Conversion</b>
</summary>
<br>

KeepDelta supports changing variables types. In that case, the delta is simply the new value.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = "hello"

>>> # Updated data
>>> new = 3.14

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
3.14  # Type changed from string to float
```
<br>
</details>

<details>
<summary>
    <b>No‑Change Cases</b>
</summary>
<br>

If no differences are found between the two inputs, KeepDelta returns the special token `__nothing__`, indicating that no changes are needed.

#### Example:

```python
>>> import keepdelta as kd

>>> # Initial data
>>> old = "hello"

>>> # Updated data
>>> new = "hello"

>>> # Create delta
>>> delta = kd.create(old, new)
>>> print(delta)
"__nothing__"  # Both inputs are identical
```
<br>
</details>

## Supported Python Versions

KeepDelta has been tested and verified to work with Python versions **3.7** to **3.13**. While it is expected to work with older versions, they have not been tested and are not officially supported.

## Contributing

Contributions are welcome! Feel free to:
* Report issues.
* Submit feature requests.
* Create pull requests.

## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/aslan-ng/keepdelta/blob/main/LICENSE) for more information.