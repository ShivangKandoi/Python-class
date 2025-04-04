# Input a string
string = input("Enter a string: ")

# Convert to uppercase
uppercase_string = ""
for char in string:
    if 'a' <= char <= 'z':  # Check if the character is lowercase
        uppercase_string += chr(ord(char) - 32)  # Convert to uppercase
    else:
        uppercase_string += char
print("Uppercase String:", uppercase_string)

# Count vowels
vowels = "AEIOU"
vowel_count = 0
for char in uppercase_string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# Check if the string is a palindrome
cleaned_string = ""
for char in string:
    if char.isalnum():  # Keep only alphanumeric characters
        cleaned_string += char.lower()

reversed_string = cleaned_string[::-1]
if cleaned_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")