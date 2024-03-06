def all_elements_true(input_tuple):
    return all(input_tuple)

# Example usage:
my_tuple = (True, True, True, True)
result = all_elements_true(my_tuple)

if result:
    print("All elements in the tuple are true.")
else:
    print("Not all elements in the tuple are true.")