import pytest
# from ingoodhands.tests.utils import faker
from ingoodhands.tests.data import CATEGORIES, INSTITUTIONS, DONATIONS, USERS
from ingoodhands.tests.utils import create_categories, create_institutions, create_donations, create_users

@pytest.fixture
def setup():
    create_categories(CATEGORIES)
    create_institutions(INSTITUTIONS)
    create_donations(DONATIONS)

@pytest.fixture
def add_users():
    create_users(USERS)

