"""
   Description: Count the occurrences of each python keyword
   Output: See Below
   Known bugs: none
"""

import keyword
from collections import Counter


def count_python_keywords(filename):
    try:
        file = open(filename, "r")
        file_content = file.read().split()
        file.close()

        keywords = []
        for word in file_content:
            if word in keyword.kwlist:
                keywords.append(word)
        return Counter(keywords)
    except FileNotFoundError:
        return "File Not Found Error" + filename
    except Exception as e:
        return f"An error occurred: {e}"


python_filename = input("Enter the python file name: ")
keyword_list_count = count_python_keywords(python_filename)
if keyword_list_count:
    for keyword, count in keyword_list_count.items():
        print(f"{keyword}: {count}")




"""
Output
class: 1
def: 5
if: 5
return: 4
True: 1
False: 1
while: 3
or: 2
try: 1
break: 2
for: 1
in: 1
continue: 1
elif: 3
"""
