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

</div>

![Header Image](https://raw.githubusercontent.com/aslan-ng/keepdelta/refs/heads/main/assets/header.png)

*KeepDelta* is a lightweight Python library designed to efficiently track and manage changes (deltas) between Python built-in types. It is applicable to various scenarios  that require dynamic data management, especially when incremental numerical changes are present, such as simulations and sensing. While many alternative tools operate at the binary level, KeepDelta emphasizes human-readable delta encoding, facilitating debugging and analysis for Python developers and researchers across multiple domains.

## What is Delta Encoding?
In many computational scenarios, efficiently managing evolving data is crucial. Traditional methods, that rely on full-state encoding — which means storing and/or transmitting complete snapshots at each step — can be inefficient due to the large size of the snapshots. Delta encoding addresses this challenge by capturing and applying only the changes (deltas) between successive states of data structures, resulting in significantly smaller and more manageable data.

<div align="center">
    <img src="https://raw.githubusercontent.com/aslan-ng/keepdelta/refs/heads/main/assets/delta_encoding.png" alt="Comparison between traditional data management method and delta encoding." width="500">
    </br>
    Managing evolving data structures by full-state encoding (left) vs. delta encoding (right).
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

1. `create(old, new)`:
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

2. `apply(old, delta)`:
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
For more usage examples, refer to the [`examples`](https://github.com/aslan-ng/KeepDelta/tree/main/examples) folder in the project repository.

## Surpported Formats
KeepDelta supports common native Python data structures, ensuring compatibility and flexibility when working with a wide variety of data types. The currently supported structures include:

* Primitive Types:
	* bool – e.g., True, False
    * str – e.g., "hello", "world"
	* int – e.g., 42, -7
	* float – e.g., 3.14, -0.001
	* complex – e.g., 3+4j, -2j
    * None

* Collections:
    * dict – e.g., {"location": "world", "age": 30}
    * list – e.g., [1, True, "hello"]
    * tuple – e.g., (2, {"location": "world"}, 3.14)
    * set – e.g., {1, 2, "apple"}

KeepDelta supports deeply nested combinations of variables, enabling structures like dictionaries of dictionaries, lists of sets, and other complex, interwoven data types.

Additionally, changing variables types are also supported. For example, changing string (like "hello") to float (like 3.14).

## Supported Python Versions
KeepDelta has been tested and verified to work with Python versions **3.7** to **3.13**. While it is expected to work with older versions, they have not been tested and are not officially supported.

## Contributing
Contributions are welcome! Feel free to:
* Report issues.
* Submit feature requests.
* Create pull requests.

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.