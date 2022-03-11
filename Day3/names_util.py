#!/usr/bin/env python3
"""
names_util module contains a few functions for manipulating names
"""
def get_intials(names):
    "this function returns intials of the given name"
    names_list = names.split()
    intials = ''
    for name in names_list:
        intials = intials + name[0].upper() + '.'
    return intials
def has_correct_format(all_names, accepted_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    """This function checks if the given name is
    in the correct format or not.
    """
    correct_format = False
    # Make a list containing both first and last names by splitting the input
    names_list = all_names.split()
    # Check if the list has at least one name.
    if len(names_list) > 0:
        # chech each name
        for name in names_list:
            #check each character in the name
            for char in name:
                #if the character is not in the accepted_chracters return false
                if char not in accepted_characters:
                    return correct_format       
        correct_format = True
    return correct_format
