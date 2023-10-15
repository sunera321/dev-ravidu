# Define a function to check if a number is prime
def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Check for factors up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If a factor is found, the number is not prime
    return True  # If no factors are found, the number is prime

# Define a function to find prime numbers in a given interval
def find_primes_in_interval(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):  # Check if each number in the interval is prime
            prime_numbers.append(num)  # If prime, add it to the list of prime numbers
    return prime_numbers  # Return the list of prime numbers

# User input for the start and end of the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Find and display the prime numbers in the specified interval
prime_numbers = find_primes_in_interval(start, end)
print("Prime numbers in the interval:", prime_numbers)
