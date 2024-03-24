import time

def read_filtered_words(path):
    with open(path, 'r') as file:
        words = file.read().splitlines()
    return words

def can_form_word(word, letter_pool):
    for letter in word:
        if letter_pool.count(letter) < word.count(letter):
            return False
    return True

def remove_letters(letter_pool, word):
    for letter in word:
        letter_pool = letter_pool.replace(letter, '', 1)
    return letter_pool

def count_three_letter_words(path):
    return sum(1 for word in path if len(word) == 3)

def write_results_to_file(results, current_set_index):
    file_path = f"C:/Users/[YourUserName]/Downloads/Valid_Sets_{current_set_index}.txt"
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{', '.join(result)}\n")
    print(f"Output written to {file_path}")

def find_words(letter_pool, words_list, path, results, first_word_counts, set_count, current_set):
    if len(path) == 12:
        # Your criteria checks here
        if count_three_letter_words(path) == 2 and 'quit' in path:
            sorted_path = sorted(path)  # Ensuring uniqueness
            if sorted_path not in results:
                results.append(sorted_path)
                print(f"\nFound valid set: {sorted_path}")
                set_count[0] += 1
                first_word_counts[path[0]] += 1  # Increment usage count for the starting word
                
                # Write results to file at each 1000 sets found or when a word reaches its limit
                if set_count[0] % 100000 == 0 or first_word_counts[path[0]] == 100000:
                    write_results_to_file(results, current_set[0])
                    results.clear()
                    current_set[0] += 1

    else:
        for word in words_list:
            if word not in path and can_form_word(word, letter_pool):
                new_letter_pool = remove_letters(letter_pool, word)
                find_words(new_letter_pool, words_list, path + [word], results, first_word_counts, set_count, current_set)

def main():
    words_list = read_filtered_words("C:/Users/[YourUserName]/Downloads/Filtered_BIP-39_Word_List.txt")
    scrambled_letters = "pqnioeuoeheispfppspmecsacaosohegntigujgpeiafss"
    
    # Make sure 'quit' is accounted for outside the loop
    scrambled_letters = remove_letters(scrambled_letters, 'quit')
    
    results = []
    first_word_counts = {word: 0 for word in words_list}
    current_set_index = [1]

    # Add 'quit' back to the pool for each set formation
    for word in words_list:
        if first_word_counts[word] < 10:  # Only proceed if the word hasn't reached its usage limit
            temp_scrambled_letters = scrambled_letters + 'quit'
            find_words(temp_scrambled_letters, words_list, [word, 'quit'], results, first_word_counts, [0], current_set_index)
            if first_word_counts[word] >= 10:
                print(f"Word '{word}' has been retired after initiating 10 sets.")

    if results:
        # Ensure any remaining results are written to a file
        write_results_to_file(results, current_set_index[0])

    print("\nProcess completed. Check the output files in your Downloads folder.")

if __name__ == "__main__":
    main()
