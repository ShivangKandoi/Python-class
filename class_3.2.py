n = int(input("Enter the number of terms in the Fibonacci series: "))

# First two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=' ')
        # Update values
        nth = a + b
        a = b
        b = nth
        count += 1