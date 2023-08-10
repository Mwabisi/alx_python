#!usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    
    # Iterate through the elements in set_1
    for element in set_1:
        # If the element is in set_2, add it to the common set
        if element in set_2:
            common.add(element)
    
    return common

# Example usage
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}

common_elements_set = common_elements(set_1, set_2)
print(common_elements_set)
