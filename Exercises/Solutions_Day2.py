#! /usr/bin/env python3
import sys

import random
def randomseq(length=1):
    """ Generate a random sequence of length `length`.
    :param length: The length of the sequence (number of bases).
    :type length: int
    
    :return: A sequence of random nucleotide base letters 'a', 'c', 'g', 't' and 'n'.
    :rtype: list
    """
    # Get a random list of letters.
    seq = random.choices(population='acgtn', k=length, cum_weights=[249,498,747,996,1000])
    
    # Return as a single string.
    return "".join(seq)

sequence = randomseq(1024)

# Save the sequence length.
sequence_length = len(sequence)

# Convert to lower case letters.
sequence = sequence.lower()

# Test if non-nucleotide letter in the sequence.
alphabet = ['a', 'c', 'g', 't', 'n']

# Setup a dictionary that will hold the counts for each nucleotide
counts = {'a':0,
          'c':0,
          'g':0,
          't':0,
          'n':0,
          }
# Test for non-nucleotide letters.
if 'n' in sequence:
        print ("Found at least one undetermined nucleotide base.")
   
for base in sequence:
    # Can also test for non-nucleotide letters here.
    if base not in alphabet:
        print ("Found non-nucleotide letter {} in sequence. Program aborts.".format(base))
        sys.exit(1)
   
    # Increment the count for this base.
    counts[base] += 1

# CG content.
cg_positions = []
current_position=0
offset=0
# Iterate through the sequence and find all occurences of 'cg'. Append position to a list.
# Since `find` returns the position of the first occurence, we have to start at the last found position 
# in each iteration.
while 'cg' in sequence[current_position:]:
    cg_position = offset + sequence[current_position:].find('cg')
    cg_positions.append(cg_position)
    current_position = cg_position+1
    
    # Save the current position as offset for the next
    offset = current_position
    
    if current_position >= sequence_length:
        break
        
# GC content.
gc_positions = []
current_position=0
offset=0
while 'gc' in sequence[current_position:]:
    gc_position = offset + sequence[current_position:].find('gc')
    gc_positions.append(gc_position)
    current_position = gc_position+1
    offset = current_position
    
    if current_position >= sequence_length:
        break

# Start codons
start_codon = 'atg'
start_codon_positions = []
current_position=0
offset=0
while start_codon in sequence[current_position:]:
    start_codon_position = offset + sequence[current_position:].find(start_codon)
    start_codon_positions.append(start_codon_position)
    current_position = start_codon_position+1
    offset = current_position
    
    if current_position >= sequence_length:
        break

# All triplets
triplets = [sequence[start:start+3] for start in range(sequence_length-3)]
triplets = [triplet for triplet in triplets if 'n' not in triplet]

# Convert to set.
unique_triplets = set(triplets)
# Print the results

print("\n")
print("Your sequence [{}]: {}".format(sequence_length, sequence))
print("\n")
print("Base report")
print("Base\tAbs. freq.\tRel. freq")
print("-"*30)
for base, count in counts.items():
    print("{0:s}\t{1:d}\t{2:f}".format(base, count, count/sequence_length))
print("\n")
print('Number of CG/GC pairs / number of pairs : {0:f}'.format(len(cg_positions+gc_positions)/(sequence_length-1)))
print("\n")
print('Start codons ATG [{}]: {}'.format(len(start_codon_positions), start_codon_positions))
print('\n')
print("Unique triplets [{}]: {}".format(len(unique_triplets), sorted(unique_triplets)))
      


