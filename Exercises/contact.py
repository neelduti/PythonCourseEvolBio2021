#! /usr/bin/env python3

contact = {
    'first name': None,
    'last name': None,
    'age': None,
    'phone': None,
    'street': None,
    'house number': None,
    'city': None,
    'zip code': None,
}

for key in contact.keys():
    contact[key] = input("Please enter your {}: ".format(key))
    
print("Your contact card:") 
print("{} {}".format(contact['first name'], contact['last name'])) 
print("{} {}".format(contact['street'], contact['house number'])) 
print("{} {}".format(contact['zip code'], contact['city'])) 
print("\n")
print("phone: {}".format(contact['phone']))

# items gives an iterable that consists of (key, value) pairs.
print(contact.items())
# keys: all keys in the dictionary
print(contact.keys())
# values: all values of the dictionary
print(contact.values())

items = [it for it in contact.items()]
keys = [k for k in contact.keys()]
values = [v for v in contact.values()]

print([it == (k,v) for it,k,v in zip(items, keys, values)])