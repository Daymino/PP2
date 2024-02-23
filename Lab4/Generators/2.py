def even_numbers_generator(n):
    return (i for i in range(0, n + 1, 2))

def main():
    try:
        n = int(input())
        even_numbers = even_numbers_generator(n)
        print(f"Even numbers between 0 and {n} in comma-separated form: {','.join(str(num) for num in even_numbers)}")
    except ValueError:
        print("Please enter a valid integer for n.")

if __name__ == "__main__":
    main()