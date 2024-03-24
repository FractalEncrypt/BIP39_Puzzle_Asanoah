# BIP39_Puzzle_Asanoah
A few files related to testing Asanoah's BIP39 painting puzzle. This is not production-ready code, it is just bare-bones POC code.
Here is a link to his puzzle post on Twitter ->
https://x.com/asanoha_gold/status/1768551394749944252

Here is some info on the files in this repo;
# AsanoahScript.py - 
This is the script I ran using the Filtered BIP-39 word list

# Truncated_BIP-39_Word_List.txt - 
This is a list of all 2048 BIP-39 words (English) that have been truncated to a maximum of 4 characters.
This was created because Asanoah posted "I have provided the first 4 letters of 10 words, and all 3 letters of 2 words."
here -> https://x.com/asanoha_gold/status/1769780999863566512

# Filtered_BIP-39_Word_List.txt
This is a list of truncated words that can be built from the provided character set

# Valid_Sets_1.txt
There are a series of Valid Sets files. These are valid sets of 12 words that are created by building up from the provided character sets.
Each set has no repeated words, and there are no duplicate sets within each file. 
I did combine the sets into a single file and checked for duplicates and came up with 131,000 unique valid sets out of 240,000.

You can verify this by running Valid_Sets_1-4.txt against VerifySets.py

# VerifySets.py
A simple script to verify if a txt file containing valid 12-word sets comtains any duplicate sets.

# AsanoahScript.No_quit.py
This is a modified version of AsanoahScript.py that was created to remove "quit" from the available words.

# Notes
- We know it is a BIP-39 seed - https://x.com/asanoha_gold/status/1768754706946445725
- We know there are no repeated words - https://x.com/asanoha_gold/status/1769582971999101117
- We know there are exactly two 3-letter words - https://x.com/asanoha_gold/status/1769780999863566512
- We know the address where the sats are - bc1qrtm29up092l9k25jmdh49wp34x78hpg4pl9puh

