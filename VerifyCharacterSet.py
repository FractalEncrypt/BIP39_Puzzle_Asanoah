def verify_sets_against_scrambled_letters(file_path, scrambled_letters):
    scrambled_sorted = ''.join(sorted(scrambled_letters.lower()))
    valid_sets_count = 0
    invalid_sets_count = 0

    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            words_in_set = line.strip().lower().split(', ')
            set_letters = ''.join(sorted(''.join(words_in_set)))

            if set_letters != scrambled_sorted:
                print(f"Line {line_num} does not match scrambled letters: {line.strip()}")
                invalid_sets_count += 1
            else:
                print(f"Line {line_num} is a valid set: {line.strip()}")
                valid_sets_count += 1
            print(f"Sorted set letters: {set_letters}")
            print(f"Sorted scrambled letters: {scrambled_sorted}\n")

    print(f"Total valid sets: {valid_sets_count}")
    print(f"Total invalid sets: {invalid_sets_count}")

if __name__ == "__main__":
    # Adjust the file path and scrambled letters as needed
    file_path = "C:/Users/[YourUserName]/Downloads/Valid_Sets_acqu_1.txt"
    scrambled_letters = "pqnioeuoeheispfppspmecsacaosohegntigujgpeiafss"
    verify_sets_against_scrambled_letters(file_path, scrambled_letters)
