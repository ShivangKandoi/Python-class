# Input a string
string = input("Enter a string: ")

# Count occurrences of each character
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Remove duplicate characters while maintaining order
unique_chars = ""
for char in string:
    if char not in unique_chars:
        unique_chars += char

# Print the results
print("Character occurrences:")
for char, count in char_count.items():
    print(f"{char}: {count}")

print("String after removing duplicates:", unique_chars)