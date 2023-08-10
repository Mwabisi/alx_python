#!usr/bin/python3

def common_elements(set_1, set_2):
    return list(set_1 & set_2)

test_cases = [
    ({"Python", "C", "Javascript"}, {"Bash", "C", "Ruby", "Perl"}),
    ({"Python", "Javascript"}, {"Bash", "C", "Ruby", "Perl"}),
    ({"Python", "Javascript"}, {"Python", "Javascript"}),
    ({"Python"}, {"Bash"}),
    ({"Python"}, {"Python"}),
    ({"Python", "C", "Javascript"}, set()),
    (set(), {"Python", "C", "Javascript"}),
    (set(), set())
]

# Perform tests and print results
for idx, (set_1, set_2) in enumerate(test_cases, start=1):
    common_elements_list = common_elements(set_1, set_2)
    print(f"Correct output - case {idx}: {common_elements_list}")
