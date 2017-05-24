dict_list = open('filtered.txt', 'r')
dict_all = dict_list.read()
dict_arr = dict_all.split()
dict_list.close()

print("start sort")

dict_arr.sort()

print("end sort")

dictionary_sort = open("dictionary_sorted.txt", 'w')
dictionary = open("f-dictionary.txt", 'w')
dict_arr_set = list(set(dict_arr))
dict_arr_set.sort()

for x in range(len(dict_arr_set)):
    word = dict_arr_set[x]
    dictionary_sort.write(word+"\n")
    dictionary.write(word+"\n")
dictionary_sort.close()
dictionary.close()
