import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000.0)  
    result = math.sqrt(number)
    return result

# Example usage:
input_number = int(input())
delay_duration = int(input())

result = delayed_square_root(input_number, delay_duration)

print(f"Square root of {input_number} after {delay_duration} milliseconds is {result}")