def count_words(text):
    # Split the text into words based on spaces
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Count the number of words in the input
    word_counter = count_words(user_input)
    
    # Display the word count
    print(f"The number of words in the given text is: {word_counter}")

main()