# Function to alternate characters in a string
def alternate_characters(string):
    result = ''  # Initialize an empty string to store the result
    for i in range(len(string)):  # Iterate through each character in the input string
        if i % 2 == 0:  # If the index is even
            result += string[i].upper()  # Convert the character to uppercase and append to result
        else:  # If the index is odd
            result += string[i].lower()  # Convert the character to lowercase and append to result
    return result  # Return the final result

# Function to alternate words in a string
def alternate_words(string):
    words = string.split()  # Split the input string into a list of words
    result = []  # Initialize an empty list to store the result
    for i, word in enumerate(words):  # Iterate through each word in the list along with its index
        if i % 2 == 0:  # If the index is even
            result.append(word.lower())  # Convert the word to lowercase and append to result
        else:  # If the index is odd
            result.append(word.upper())  # Convert the word to uppercase and append to result
    return ' '.join(result)  # Join the words in the result list to form the final string

# Test the functions
input_string = "Hello World"
print("Original String:", input_string)
print("Alternate Characters:", alternate_characters(input_string))

input_string = "I am learning to code"
print("Original String:", input_string)
print("Alternate Words:", alternate_words(input_string))
