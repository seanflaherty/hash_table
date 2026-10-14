"""This class implements a basic Hash Table data structure."""
from typing import Any
class HashTable:
    """Initializes the class."""
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        """The hash of the supplied string."""
        # Calculates the sum of the Unicode values of each character
        return sum(ord(char) for char in string)

    def add(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair."""
        hash_key = self.hash(key)

        # If the hash key doesn't exist in the collection, initialize a nested dictionary
        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        # Store the key-value pair inside the nested dictionary at that hash index
        self.collection[hash_key][key] = value

    def remove(self, key: str) -> None:
        """Delete a key-value pair from the hash table."""
        hash_key = self.hash(key)

        # Guard clause: check if the hash_key and the target key exist before deleting
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key: str) -> Any:
        """Finds and returns the value associated with the provided key."""
        hash_key = self.hash(key)

        # Check if hash_key and key exist, then return the corresponding value
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]

        return None
