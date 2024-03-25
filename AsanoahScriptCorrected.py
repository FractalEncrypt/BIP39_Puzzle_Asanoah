import os
import time

def read_filtered_words(path):
    with open(path, 'r') as file:
        return file.read().splitlines()

def can_form_word(word, letter_pool):
    for letter in word:
        if letter_pool.count(letter) < word.count(letter):
            return False
    return True

def remove_letters(letter_pool, word):
    for letter in word:
        letter_pool = letter_pool.replace(letter, '', 1)
    return letter_pool

def read_global_sets(path):
    global_sets = set()
    if os.path.exists(path):
        with open(path, 'r') as file:
            global_sets = set(line.strip() for line in file.readlines())
    return global_sets

def add_to_global_sets(path, new_sets):
    with open(path, 'w') as file:
        for new_set in new_sets:
            file.write(f"{new_set}\n")

def write_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result}\n")
    print(f"Output written to {file_path}")

def find_words(letter_pool, words_list, path, results, qu_word, qu_word_set_count, total_set_count, total_tries, output_file_counter, global_sets):
    if total_tries[0] % 100 == 0:
        print(f"\rProcessing... Qu word '{qu_word}': Total tries: {total_tries[0]}, Sets found: {total_set_count[0]}", end='')

    if len(path) == 12:
        sorted_path_str = ', '.join(sorted(path))
        if sorted_path_str not in global_sets:
            global_sets.add(sorted_path_str)
            results.append(sorted_path_str)
            qu_word_set_count[0] += 1
            total_set_count[0] += 1
            print(f"\nQu word '{qu_word}': Found set #{qu_word_set_count[0]} with {qu_word}. Total valid sets: {total_set_count[0]}, Total tries: {total_tries[0]}")
            print(f"Found valid set: {sorted_path_str}")
            if len(results) >= 10000:
                output_file_path = f"C:/Users/[YourUserName]/Downloads/Valid_Sets_{qu_word}_{output_file_counter[0]}.txt"
                write_results_to_file(results, output_file_path)
                results.clear()
                output_file_counter[0] += 1
    else:
        for word in words_list:
            total_tries[0] += 1
            if word not in path and can_form_word(word, letter_pool):
                find_words(remove_letters(letter_pool, word), words_list, path + [word], results, qu_word, qu_word_set_count, total_set_count, total_tries, output_file_counter, global_sets)

def main():
    filtered_word_list_path = "C:/Users/[YourUserName]/Downloads/Filtered_BIP-39_Word_List3.txt"
    global_sets_path = "C:/Users/[YourUserName]/Downloads/Global_Valid_Sets.txt"
    scrambled_letters = "pqnioeuoeheispfppspmecsacaosohegntigujgpeiafss"

    words_list = read_filtered_words(filtered_word_list_path)
    global_sets = read_global_sets(global_sets_path)
    words_with_qu = [word for word in words_list if "qu" in word]

    total_set_count = [0]
    total_tries = [0]
    output_file_counter = [1]

    for qu_word in words_with_qu:
        qu_word_set_count = [0]
        results = []
        temp_letter_pool = remove_letters(scrambled_letters, qu_word)
        print(f"\nProcessing sets with starting 'qu' word: {qu_word}")
        find_words(temp_letter_pool + qu_word, words_list, [qu_word], results, qu_word, qu_word_set_count, total_set_count, total_tries, output_file_counter, global_sets)
        if results:
            output_file_path = f"C:/Users/[YourUserName]/Downloads/Valid_Sets_{qu_word}_Final.txt"
            write_results_to_file(results, output_file_path)

    print("\nProcess completed. Total valid sets found: {}, Total tries: {}".format(total_set_count[0], total_tries[0]))

if __name__ == "__main__":
    main()
