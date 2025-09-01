#program for accepting list of words and find max length words
#MaxLengthWordsEx1.py

def get_words():
    """
    Prompts the user to enter words one by one and stops when '@' is entered.
    Returns a list of entered words.
    """
    print("Enter a list of words (press '@' to stop):")
    words = []
    while True:
        word = input()
        if word == "@":
            break
        words.append(word)
    return words


def find_max_len_words(words):
    """
    Finds and prints the word(s) with the maximum length in the given list.
    Also prints the number of such words.
    """
    if not words:
        print("The list is empty -- can't find max length word.")
        return

    # Create a dictionary with words as keys and their lengths as values
    word_lengths = {word: len(word) for word in words}

    # Find the maximum length
    max_length = max(word_lengths.values())

    # Find all words with the maximum length
    max_length_words = [word for word, length in word_lengths.items() if length == max_length]

    # Display results
    print("\nWord lengths:", word_lengths)
    print(f"Max length words (length = {max_length}):")
    for word in max_length_words:
        print(f"\t{word}")
    print(f"Number of max length words: {len(max_length_words)}")


# Main Program
if __name__ == "__main__":
    words = get_words()
    find_max_len_words(words)
