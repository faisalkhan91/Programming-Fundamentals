"""
Amazon phone interview (white board) question.

Return a list of all the words in a given list, where the letters in the given string matches the letters in the words
that are given. Each word can have some or all the letters in the given string in any order but cannot exceed the
frequency of the letters in the string.

Example:
Input:
    letter = ogd
    list_of_words = [cab, ab, go, od, odg, god, good, back]
Output:
    [go, od, odg, god]
"""


def similar_words(list_of_words, letters):
    letters_list = list(letters)
    similar = []
    flag = True

    for word in list_of_words:
        word = list(word)
        if len(word) <= len(letters_list):
            for i in word:
                if i not in letters_list:
                    flag = False
            if flag:
                similar.append(word)
            else:
                flag = True

    return similar


letters = "ogd"
list_of_words = ["cab", "ab", "go", "od", "odg", "god", "good", "back"]
print(similar_words(list_of_words, letters))
