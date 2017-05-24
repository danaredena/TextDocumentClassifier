import os
import re

ex_list = open('exception.txt', 'r')
ex_all = ex_list.read()
ex_arr = ex_all.split()
ex_list.close()

def char_check(char):
    if (char.isalpha()):
        return True
    if (char.isdigit()):
        return True
    return False

def pre_word(word):
    if (word==""):
        return ""
    while (char_check(word[-1]) == False):
        if (len(word) == 1):
            return ""
        word = word[:-1]

    while (char_check(word[0]) == False):
        if (len(word) == 1):
            return ""
        word = word[1:]

    return word.lower()

def dict_bin(word, word_array):
    if (word.isdigit()):
        return True
    elif (re.match("[0-9]+\.[0-9]+", word)):
        return True
    elif (re.match("[0-9]{1,3}(,[0-9]{1,3})+", word)):
        return True

    i = 0
    j = len(word_array) - 1
    while (j >= i):
        mid = int((i+j)/2)
        if (word_array[mid] == word):
            return True
        if (max(word, word_array[mid]) == word):
            i = mid + 1
        else:
            j = mid - 1
    return False

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data/"
dir_path = os.path.join(script_dir, rel_path)

def readFile(filename):
    textfile = open(filename)
    text_all = textfile.read()
    textfile.close()
    return re.split("[\s,]",text_all)

dictionary = open("dictionary.txt", 'w')

for count in range(11307):
    print(count)
    file_path = os.path.join(dir_path, str(count))
    text_arr = readFile(file_path)
    for x in range(len(text_arr)):
        word = pre_word(text_arr[x])
        if (word != "" and dict_bin(word, ex_arr) == False):
            dictionary.write(word+"\n")
dictionary.close()
