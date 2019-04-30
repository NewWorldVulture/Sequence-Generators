# Created by Ada
# Should probably be considered a beta version of this
# There has to be a way to separate a string into a list by character-type

# Iterates a look-and-say sequence once using a default offset of 0. (regular look-and-say)
# Passing in an offset of 1 moves 1 element of the sequence to the end, then continues the look-and-say iteration

def next_iteration(sequence, offset=0):
    result = ''
    pointer = 0
    sequence = sequence[offset:] + sequence[:offset]
    
    # Still feels clunky
    while pointer < len(sequence):
        # Counts the quantity of each digit
        count = 1
        while pointer + 1 < len(sequence) and sequence[pointer] == sequence[pointer+1]:
            pointer += 1
            count += 1
        result += str(count) + sequence[pointer]
        pointer += 1
    return result
