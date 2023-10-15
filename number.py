def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_interval(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# User input
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

prime_numbers = find_primes_in_interval(start, end)
print("Prime numbers in the interval:", prime_numbers)
