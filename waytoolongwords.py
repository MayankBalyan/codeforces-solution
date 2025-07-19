def abbreviate_word(word):
    """
    Abbreviates a word if its length is greater than 10 characters,
    otherwise returns the original word.
    """
    if len(word) <= 10:
        return word
    else:
        return word[0] + str(len(word) - 2) + word[-1]

# Example usage:
num_words = int(input())  # Number of words to process
for _ in range(num_words):
    current_word = input()
    print(abbreviate_word(current_word))