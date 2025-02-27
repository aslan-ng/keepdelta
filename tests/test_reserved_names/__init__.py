"""
There are a few string values that are reserved for internal use. These
variables are used to store information about the changes that have been made
to the object. The reserved variables can be found in the `keepdelta.config`
module.

The reserved variables are:
- `keys["nothing"]`: This key is used to indicate that no change is detected.
- `keys["delete"]`: This key is used to indicate that a key in a dictionary has
  been deleted.
- `keys["add to set"]`: This key is used to indicate that an element in a set has been
  added.
- `keys["remove from set"]`: This key is used to indicate that an element in a set has
  been removed.

Here the conflicts are checked for the reserved variables that may cause unpredictable results.
"""