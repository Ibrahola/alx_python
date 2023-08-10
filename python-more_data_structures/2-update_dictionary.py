# def replace_or_add(dictionary, key, value):
#     for k in my_dict:
#         dictionary[key] = value

# # Example usage
# # my_dict = {'a': 1, 'b': 2}
# my_dict = {'language': "C", 'number': 89, 'track': "Low level"}
# new_dict = replace_or_add(my_dict, 'language', "python")

# # replace_or_add(my_dict, 'c', 3)  # Adds 'c': 3 to the dictionary
# # replace_or_add(my_dict, 'a', 5)  # Replaces 'a' value with 5
# # print(my_dict)  # Output: {'a': 5, 'b': 2, 'c': 3}

# print(my_dict)

def print_sorted_dictionary(my_dict):
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))


a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}