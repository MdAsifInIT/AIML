# PRIME NUMBER: Check if number is prime
# Definition: Prime number > 1 with no divisors except 1 and itself
# Properties:
# - 2 is the smallest prime number
# - All primes > 2 are odd
# - Check divisibility from 2 to n-1
# Algorithm: If any number from 2 to n-1 divides n, then n is NOT prime

import math  # Math module (for potential optimization)

def prime(a):
    """Check if number a is prime. Return True if prime, False otherwise."""
    # Numbers less than 2 are not prime
    if a < 2:  # 0, 1, and negative numbers are not prime
        return False
    
    # Check if any number from 2 to (a-1) divides a
    # This is a simple approach; more efficient checks go up to sqrt(a)
    for i in range(2, (a-1)):  # Check divisibility from 2 to a-2
        if a % i == 0:  # If divisible by i
            return False  # Not prime (found a divisor)
    
    return True  # No divisors found, number is prime

# Test: Check if 2 is prime
print (prime(2))  # Output: True (2 is the smallest prime)
        