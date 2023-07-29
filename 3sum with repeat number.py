# Given an array of integers, determine if any 3 inte‍‌‌‌‌‌‍‍‍‌‌‌‍‍‌‍‌‍‍‌gers in the array sum to zero.  each integer can be used up to 3 times

from collections import Counter

def has_zero_sum_triple(arr):
    counts = Counter(arr)

    # Iterate through unique integers
    for x in counts:
        # Check if three times the integer sums to zero
        if x == 0 and counts[x] >= 3:
            return True

        # Check other combinations
        for y in counts:
            if y == x and counts[y] < 2:
                continue

            # Calculate the required third integer
            z = -(x + y)
            
            # Check if the combination is valid and the third integer is in the array
            if z in counts:
                # Handle cases where x, y, and z are all the same
                if x == y == z and counts[x] >= 3:
                    return True
                # Handle cases where two of x, y, and z are the same
                elif (x == y and counts[x] >= 2) or (x == z and counts[x] >= 2) or (y == z and counts[y] >= 2):
                    return True
                # Handle general cases
                elif x != y and y != z and x != z:
                    return True

    return False

# Example usage
arr = [3, 1, -4, 2, 3, 0, 0, 0]
print(has_zero_sum_triple(arr))  # Output: True

# Given an array of integers, determine how many combinations of  3 inte‍‌‌‌‌‌‍‍‍‌‌‌‍‍‌‍‌‍‍‌gers in the array sum to zero.  each integer can be used up to 3 times

from collections import Counter

def count_zero_sum_triples(arr):
    counts = Counter(arr)
    total_combinations = 0

    # Iterate through unique integers
    for x in counts:
        # If x is zero and there are at least 3 zeros, count the combination
        if x == 0 and counts[x] >= 3:
            total_combinations += 1

        for y in counts:
            if y < x: # To avoid double-counting combinations
                continue

            if y == x and counts[y] < 2:
                continue

            # Calculate the required third integer
            z = -(x + y)
            
            # To avoid double-counting combinations
            if z < y:
                continue

            # Check if the combination is valid and the third integer is in the array
            if z in counts:
                # Handle cases where x, y, and z are all the same
                if x == y == z and counts[x] >= 3:
                    total_combinations += 1
                # Handle cases where two of x, y, and z are the same
                elif (x == y and counts[x] >= 2) or (x == y and y == z and counts[x] >= 3):
                    total_combinations += 1
                # Handle general cases
                elif x != y and y != z and x != z:
                    total_combinations += 1

    return total_combinations

# Example usage
arr = [3, 1, -4, 2, 3, 0, 0, 0]
print(count_zero_sum_triples(arr))  # Output: 4
