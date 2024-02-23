def squares_generator(a, b):
    for num in range(a, b + 1):
        yield num ** 2

# Test the generator with a for loop
def main():
    try:
        a = int(input())
        b = int(input())

        # Generate squares using the generator
        for square in squares_generator(a, b):
            print(square)

    except ValueError:
        print("Please enter valid integers for a and b.")

if __name__ == "__main__":
    main()