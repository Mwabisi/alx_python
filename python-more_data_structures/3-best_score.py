#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')  # Initialize with negative infinity

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_value:
            max_key = key
            max_value = value

    return max_key
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))