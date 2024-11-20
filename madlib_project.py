# Open the story.txt file for reading
with open("story.txt", "r") as f:
    # Read the content of the file into the variable 'story'
    story = f.read()

# Create a set to store unique words that need to be filled in
words = set()
# Initialize the position of the start of a word
start_of_word = 1

# Define the markers for the start and end of words
target_start = "<"
target_end = ">"

# Iterate over each character in the story along with its index
for i, char in enumerate(story):
    # Check if the character is the start marker
    if char == target_start:
        start_of_word = i  # Update the start position

    # Check if the character is the end marker
    if char == target_end and start_of_word != -1:
        # Extract the word enclosed by the markers
        word = story[start_of_word: i + 1]
        # Add the word to the set of words
        words.add(word)
        # Reset the start_of_word to indicate we are not inside a word anymore
        start_of_word = -1

# Dictionary to hold user inputs for each word
answers = {}

# Prompt the user for each word that needs to be filled in
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer  # Store the user's answer in the answers dictionary

# Replace each word in the story with the user's answer
for word in words:
    story = story.replace(word, answers[word])

# Print the completed story with the user's words inserted
print(story)
