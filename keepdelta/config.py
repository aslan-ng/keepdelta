"""
These are the internal variables that are reserved for internal use. These
variables are used to store information about the changes that have been made
to the object. It is possible to change them here based on specific requirements.
"""

keys = {
    "nothing": "__nothing__",  # No changes are required
    "delete": "__delete__",  # Key to be removed from dict
    "add to set": "__add__",  # Elements to be added to set
    "remove from set": "__remove__",  # Elements to be removed from set
}
