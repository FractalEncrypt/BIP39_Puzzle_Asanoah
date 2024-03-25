# BIP39_Puzzle_Asanoah
A few files related to testing Asanoah's BIP39 painting puzzle. This is not production-ready code, it is just bare-bones POC code.
Here is a link to his puzzle post on Twitter ->
https://x.com/asanoha_gold/status/1768551394749944252

Here is some info on the files in this repo;
# AsanoahScriptCorrected.py - 
This is the final script I ran using the Filtered BIP-39 word list.
(it does create valid sets)
I manually modified the Word list to change the first "qu" word it uses to build the lists. 
I wanted to "retire" words after a set number of tries, but it seems to find 10's of thousands of valid sets
with each word, so I just manually did it rather than doing it via the script.

# AsanoahScript.py - 
This is the script I ran using the Filtered BIP-39 word list
(it does not build valid sets correctly)

# AsanoahScript.No_quit.py
This is a modified version of AsanoahScript.py that was created to remove "quit" from the available words.
(it does not build valid sets correctly)

# Truncated_BIP-39_Word_List.txt - 
This is a list of all 2048 BIP-39 words (English) that have been truncated to a maximum of 4 characters.
This was created because Asanoah posted "I have provided the first 4 letters of 10 words, and all 3 letters of 2 words."
here -> https://x.com/asanoha_gold/status/1769780999863566512

# Filtered_BIP-39_Word_List.txt
This is a list of truncated words that can be built from the provided character set

# Valid_Sets.txt
Many of my first "Valid Sets" were not actually valid - either because they didn't correctly use all the scrambled characters, or
because it didn't handle the word "quit" properly, as I got off on a wrong tangent because of a tweet.

The valid sets that are correctly built are
 - Valid_Sets_acqu_(number).txt
 - Valid_Sets_quic_(number).txt

Each valid set file has 10,000 valid sets. As this amount of sets is too vast to check against the address to verify if any set is a valid seed, at this point I gave up...
This puzze is impossible for me to crack - based on these results, my available compute resources, and my skillset.

You can verify this by running Valid_Sets_1-4.txt against VerifySets.py

# VerifySets.py
A simple script to verify if a txt file containing valid 12-word sets comtains any duplicate sets.

# Notes
- We know it is a BIP-39 seed - https://x.com/asanoha_gold/status/1768754706946445725
- We know there are no repeated words - https://x.com/asanoha_gold/status/1769582971999101117
- We know there are exactly two 3-letter words - https://x.com/asanoha_gold/status/1769780999863566512
- We know the address where the sats are - bc1qrtm29up092l9k25jmdh49wp34x78hpg4pl9puh

