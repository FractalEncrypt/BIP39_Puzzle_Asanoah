def verify_unique_sets(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    # Convert each line into a sorted tuple to standardize the order of words
    sets = [tuple(sorted(line.split(', '))) for line in lines]

    # Use a set to automatically filter out any duplicates
    unique_sets = set(sets)

    # Report findings
    print(f"Total sets found: {len(lines)}")
    print(f"Unique sets found: {len(unique_sets)}")
    if len(lines) != len(unique_sets):
        print("Duplicates were found.")
    else:
        print("No duplicates were found.")

# Replace 'your_file_path_here' with the path to your file
file_path = "C:/Users/[YourUserName]/Downloads/Valid_Sets_1.txt"
verify_unique_sets(file_path)
