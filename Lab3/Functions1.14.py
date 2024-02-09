# Task 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Task 2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Task 3
def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numheads <= 0 or numlegs <= 0:
        print("No solution exists.")
        return None

    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits

    if num_rabbits < 0 or num_chickens < 0 or num_rabbits != int(num_rabbits) or num_chickens != int(num_chickens):
        print("No solution exists.")
        return None

    return int(num_chickens), int(num_rabbits)

# Task 4
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5
def print_permutations(input_string):
    for perm in permutations(input_string):
        print(''.join(perm))

# Task 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Task 7
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Task 8
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 9
def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    length = len(cleaned_word)
    
    for i in range(length // 2):
        if cleaned_word[i] != cleaned_word[length - 1 - i]:
            return False
    
    return True

# Task 10
def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

# Task 11
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Task 12
def sphere_volume(radius):
    if radius < 0:
        return "Radius must be non-negative."
    else:
        volume = (4/3) * math.pi * radius**3
        return volume

# Task 13
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Importing required modules
import random