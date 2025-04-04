# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print the first n prime numbers
def print_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1

# Input from the user
n = int(input("Enter the number of prime numbers to print: "))

# Print the first n prime numbers
print(f"The first {n} prime numbers are:")
print_n_primes(n)
