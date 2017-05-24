dict_list = open('dictionary.txt', 'r')
dict_all = dict_list.read()
dict_arr = dict_all.split()
dict_list.close()

print("start sort")

dict_arr.sort()

print("end sort")

dictionary = open("dictionary_sorted.txt", 'w')

dict_arr_set = list(set(dict_arr))
dict_arr_set.sort()

for x in range(len(dict_arr_set)):
    word = dict_arr_set[x]
    dictionary.write(word+"\n")

dictionary.close()
