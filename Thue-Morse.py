# Created by Ada
# Generates the Thue-Morse Sequence
# Takes the previous iteration of the sequence, and appends each boolean's complement.

sequence = [True]

def next_iteration(sequence):
    # Negates each element in the sequence, then appends it to the sequence
    sequence += [not x for x in sequence]
    # Print out as '1001' instead of [True, False, False, True]
    print(''.join([str(int(x)) for x in sequence]), end='\n')
    return next_iteration(sequence)

next_iteration(sequence)
