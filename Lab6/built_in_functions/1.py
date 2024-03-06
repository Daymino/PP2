from functools import reduce

def multiply_list(numbers):
    # Using the reduce function to multiply all elements in the list
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Input numbers until 1 is entered
numbers_list = []
while True:
    try:
        num = float(input("Enter a number (enter 1 to stop): "))
        if num == 1:
            break
        numbers_list.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Example usage:
result = multiply_list(numbers_list)

print(f"The product of all entered numbers is: {result}")