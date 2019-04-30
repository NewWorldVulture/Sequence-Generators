# Created by Ada
# Generates iterations of the abacabadabacaba sequence

import string, math

sequence = ''
chars = string.ascii_letters

def next_iteration(sequence):
    # The length of each sequence is a power of two minus one, so we can just add one and take the log_2
    sequence = sequence + chars[int(math.log(len(sequence)+1, 2))] + sequence
    print(sequence)
    return next_iteration(sequence)
    
next_iteration(sequence)
