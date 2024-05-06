""" 
Problem statement
You are given an integer 'n'. Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.


An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself. For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

"""


def check_Armstrong(n):
    # Temporary variable to store the value on n
    temp = n
    # Initialize sum
    sum_digits = 0
    # Count the number of digits in n
    power = len(str(n))
    # Calculate
    while temp > 0:
        digits = temp % 10
        sum_digits += digits**power
        temp //= 10

    # Check
    return sum_digits == n


n = int(input())
print(check_Armstrong(n))
