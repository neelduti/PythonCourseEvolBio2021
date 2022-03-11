#! /usr/bin/env python3

name = input("Please enter your name: ")

print("Hallo " + name + "!")

name_length = len(name)
print ("Your name is {} characters long.".format(name_length))

words_in_name = name.split(" ")
print('There are {} words in your name.'.format(len(words_in_name)))

reversed_name = name[::-1]
print("Your name read backwards reads '{}'".format(reversed_name))

every_other_letter_from_first = name[::2]
every_other_letter_from_second = name[1::2]

print("Starting from the first letter, every other letter in your name is {}".format(every_other_letter_from_first))
print("Starting from the second letter, every other letter in your name is {}".format(every_other_letter_from_second))

inverted_capitalization = [l.upper() if l.islower() else l.lower() for l in name]
print("Your name with inverted capitalization reads '{}'.".format(inverted_capitalization))

unique_letters = set(name)
print("The unique letters in your name are: {}".format(sorted(unique_letters)))

import string
alphabet = string.ascii_lowercase
ALPHABET = string.ascii_uppercase

lower_case_letters_in_name = [(l, l in unique_letters) for l in alphabet]
upper_case_letters_in_name = [(l, l in unique_letters) for l in alphabet]

print("Out of all letters in the lower case alphabet, these are in your name:")
[print(lc) for lc in lower_case_letters_in_name]
print("Out of all letters in the upper case alphabet, these are in your name:")
[print(lu) for lu in upper_case_letters_in_name]