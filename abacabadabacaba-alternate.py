# Created by Ada
# Alternate, funkier way to generate the first n digits of an abacaba sequence
# Takes advantage of a feature in binary numbers

import string
chars = string.ascii_letters

def get_abacaba(n):
    # Converts the first n integers into binary, and counts the number of...
    # ... '0's at the end. If none, add 'a'. If one, add 'b'. If two add 'c', etc.
    sequence = [chars[bin(i).split('1')[-1].count('0')] for i in range(1,n)]
    return sequence
