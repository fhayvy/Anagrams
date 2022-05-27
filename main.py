# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    edited_word = word.replace(" ", "")
    edited_anagram = anagram.replace(" ", "")
    if sorted(edited_word) == sorted(edited_anagram):
        return True
    else:
        return False
word1 = input("What's the first word?: ")
word2 = input("What's the second word?: ")

find = find_anagram(word1, word2)

if find:
    print(f"{word1} and {word2} are anagrams.")
    print(find)
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
    print(find)
