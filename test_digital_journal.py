# Tests for the functions in project.py
import pytest
import os
import csv
from project import register, login, new_journal, new_entry, valid_date

@pytest.fixture
def test_users():
    # Create a temporary users file for testing
    return "tests/test_users.csv"

@pytest.fixture
def test_journal():
    # Create a temporary journal for testing
    return "tests/test_journal.csv"

def test_register(test_users):
    # Test registering a new user
    assert register(test_users, "test_user", "pw123") is True
    assert register(test_users, "test_user2", "pw222") is True
    # Test registering an existing user
    assert register(test_users, "test_user", "pw123") is False

def test_login(test_users):
    # Test logging in with correct username and password
    assert login(test_users, "test_user", "pw123") is True
    # Test logging in with incorrect password
    assert login(test_users, "test_user", "pw000") is False
    # Test logging in with incorrect username
    assert login(test_users, "no_user", "pw123") is False

def test_valid_date():
    # Test invalid dates and format
    assert valid_date("2024/02/15") == False
    assert valid_date("2024-2-15") == False
    assert valid_date("2024-15-01") == False
    assert valid_date("2024-12-40") == False
    assert valid_date("2024-02-15") == True

"""
def test_new_journal(test_journal):
    # Test creating a new journal
    new_journal(test_journal)
    # Test that the new journal exists
    assert os.path.exists(test_journal) is True
    # Test if journal has correct headers
"""
