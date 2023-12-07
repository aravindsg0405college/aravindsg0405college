"""
   Description: String permutation
   Output: See Below
   Known bugs: none
"""


def displayPermutations(s):
    displayPermutationsHelper("", s)


def displayPermutationsHelper(s1, s2):
    if len(s2) == 0:
        print(s1)
    else:
        for i in range(len(s2)):
            new_s1 = s1 + s2[i]
            new_s2 = s2[:i] + s2[i+1:]
            displayPermutationsHelper(new_s1, new_s2)


def is_single_word(word):
    return len(word.split()) == 1


input_word = input("Enter a single word: ")


if is_single_word(input_word):
    displayPermutations(input_word)
else:
    print("Please enter a single word, not a sentence.")

"""
Output
Enter a single word: ABC
ABC
ACB
BAC
BCA
CAB
CBA

Enter a single word: Hello World
Please enter a single word, not a sentence.

"""