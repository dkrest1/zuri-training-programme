# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # checking the length of both words
    if len(word) == len(anagram):
        # sorting both words and storing them in avariable
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        # checking if both are the same through the comparison operator
        if sorted_word == sorted_anagram:
            return True
        else:
            return False


find_anagram("below", "elbow")
