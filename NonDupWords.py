"""
   Description: Diplay nonduplicate words in ascending order
   Output: See Below
   Known bugs: none
"""


def print_non_duplicates_words(filename):
    try:
        file = open(filename, "r")
        file_content = file.read().lower().split()
        file.close()

        unique_words = set()
        word_count = {}

        for word in file_content:
            word_count[word] = word_count.get(word, 0) + 1

        for word, count in word_count.items():
            if count == 1:
                unique_words.add(word)

        for word in sorted(unique_words):
            print(word)
    except FileNotFoundError:
        return "File Not Found Error" + filename
    except Exception as e:
        return f"An error occurred: {e}"


text_filename = input("Enter the text file name: ")
print_non_duplicates_words(text_filename)



"""
Output
break
cannot
conjunction.
down
easy
end
flauccinauccinihilipilification
has
into
no
object
pneumonoultramicroscopicsilicovolcanoconiosis
there
to
way
with
"""
