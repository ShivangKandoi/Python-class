# Input a paragraph
paragraph = input("Enter a paragraph: ")

# Split the paragraph into words
words = paragraph.split()

# Find the longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Print the longest word and its reverse
print("Longest word:", longest_word)
print("Reversed longest word:", longest_word[::-1])