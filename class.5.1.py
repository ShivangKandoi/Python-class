def print_prime_number(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
n = int(input("Enter a number: "))
print("Prime numbers up to", n, "are:")
print_prime_number(n)