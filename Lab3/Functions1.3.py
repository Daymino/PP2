#Exercise 3

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None  # No solution found

heads = 35
legs = 94

result = solve(heads, legs)

rabbits, chickens = result 

print(rabbits,chickens)