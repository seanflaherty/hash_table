"""Tests for the hash table class."""
import pytest
from src.hash_table import HashTable

@pytest.fixture
def hash_table():
    """Provides a fresh, empty HashTable instance for each test."""
    return HashTable()


def test_initialization(hash_table):
    """Test that a new hash table starts with an empty collection."""
    assert hash_table.collection == {}


def test_hash_function(hash_table):
    """Test that the hash function returns consistent and predictable results."""
    # Unicode for 'a' is 97
    assert hash_table.hash("a") == 97

    # Same string should always produce the same hash key
    assert hash_table.hash("hello") == hash_table.hash("hello")

    # Different strings should generally produce different hashes
    assert hash_table.hash("hello") != hash_table.hash("world")


def test_add_and_lookup(hash_table):
    """Test adding key-value pairs and looking them up successfully."""
    hash_table.add("apple", 10)
    hash_table.add("banana", 20)

    assert hash_table.lookup("apple") == 10
    assert hash_table.lookup("banana") == 20


def test_lookup_missing_key(hash_table):
    """Test that looking up a key that doesn't exist returns None."""
    assert hash_table.lookup("nonexistent") is None


def test_update_existing_key(hash_table):
    """Test that adding an existing key updates its value instead of duplicating."""
    hash_table.add("score", 100)
    hash_table.add("score", 150)  # Update value

    assert hash_table.lookup("score") == 150


def test_remove_key(hash_table):
    """Test removing an existing key from the hash table."""
    hash_table.add("apple", 10)
    hash_table.remove("apple")

    assert hash_table.lookup("apple") is None


def test_remove_nonexistent_key(hash_table):
    """Test that removing a key that doesn't exist handles gracefully without errors."""
    # Should not raise a KeyError or crash
    hash_table.remove("ghost_key")