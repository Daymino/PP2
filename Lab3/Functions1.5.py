from itertools import permutations

def print_permutations(input_string):
    for perm in permutations(input_string):
        print(''.join(perm))

user_input = input()
print_permutations(user_input)