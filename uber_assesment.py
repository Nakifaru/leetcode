# 1. Swap 2 numbers in a list if the first is larger
# input [6, 7, 8, 8, 5, 3, 2]
# output [6, 7, 8, 8, 3, 5, 2]

def swap(L):
    # hold the index of the first of the pair in memory
    i = 0
    # check that the second element of the pair is within the list
    while i + 1 < len(L):
        first = L[i]
        second = L[i + 1]
        # swap the pair if the first is larger than the second
        if first > second:
            L[i] = second
            L[i + 1] = first
        # Increment by 2 to get to the next pair    
        i += 2
    return L

print(swap([6, 7, 8, 8, 5, 3, 2]))

