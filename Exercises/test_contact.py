# Import the function to be tested.
from contact import print_contact_card

contact = {
    'first name': "John",
    'last name': "Doe",
    'age': 99,
    'phone': '+1-234-5678-91011',
    'street': 'Main Street',
    'house number': 33,
    'city': "Springfield",
    'zip code': 99999,
}


# Run the function
def test_print_contact_card():
    card = print_contact_card(contact)

    expected_str = """
John Doe
Main Street 33
99999 Springfield

phone: +1-234-5678-91011
"""

    assert card == expected_str


