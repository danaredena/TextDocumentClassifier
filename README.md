A text document classifier using Naive Bayes that tells the topic that the text document is most likely to be under to among the 20 topics.

This covers both the Versions 1 and 2 of the program
Programming Language: Python 3

For building the dictionary:
1) Put the training set (files) inside a folder named "data" under the directory you're working on
2) Put the files you want to classify inside a folder named "classify" still under your working directory
3) Run "dictionary.py" - reads and collects all the words in your training files and put it into "dictionary.txt". This excludes all the words in the "exception.txt"
4) Run "sorter.py" - reads "dictionary.txt" and sorts all the words in it, making sure that each word appears only once. The sorted words will then be listed in "dictionary-sorted.txt"

** Steps 5 and 6 can be skipped for Version 2 but the content of "dictionary_sorted.txt" should be copied to a "f-dictionary.txt"**
5) Run "filter.py" - reads through "dictionary-sorted.txt" and classifies certain "words"/strings according to a common format (e.g. strings who have "mb/s" under "_mb/s_") and stores it in "filtered.txt"
6) Run "sorter-2.py" - reads "filtered.txt" and sorts all the words in it, making sure that each word/string appears only once. The sorted words will then be listed in "dictionary-sorted.txt" and "f-dictionary.txt"

For the preparation of getting the probabilities:
7) Run "counter.py" - counts the number of times that each word/string in the "f-dictionary.txt" occurs in all the files under the "data" subfolder. The occurrences are recorded in the "occ_count.txt"
8) Run "category.py" - counts the number of times a certain category/classification appears in the training files and puts it in "cat_count.txt"

For the Naive Bayes (the hard stuff):
9) Run "bayes.py" - builds an array for the probabilities of the words in the final dictionary occurring for category, as well as the complement probabilities. The probabilities will then be lambda smoothed according to lambda equals 0.01, 0.1, 0.2, 0.5, 1.0. Runs through the files under the "classify" subfolder to see which words/strings that belong to the final dictionary appears in each file. Performs Maximum A Posteriori on the files under "classify" folder according to the collected information on which word/string appears on each file, the Maximum A Posteriori probabilities will vary depending on what lambda in lambda smoothing is used. The highest probability for corresponding to the 20 categories will be chosen as the classification. The file numbers with their classifications is stored in "f_classify" text files with their corresponding lambda values (e.g. "f_classify_0.01.txt" for the classifications using 0.01 as the lambda value)
10) Run "checker.py" - computes the number and percentage of correct classifications for the 0.01, 0.1, 0.2, 0.5, and 1.0 lambda values.
