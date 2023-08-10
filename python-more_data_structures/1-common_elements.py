#!usr/bin/python3
def common_elements(set_1, set_2):
    return list(set_1.intersection(set_2))

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}

common_elements_list = common_elements(set_1, set_2)
print(common_elements_list)
