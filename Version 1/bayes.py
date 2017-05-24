#============================== PROBABILITY MATRIX ==============================
occ_count = open("occ_count.txt", 'r')
occ_count_all = occ_count.read()
occ_count_list = occ_count_all.split()

cat_count_file = open("cat_count.txt", 'r')
cat_all = cat_count_file.read()
cat_count = cat_all.split()

cat_prob = []
for h in range(20):
    cat_prob.append(int(cat_count[h])/11307)

def lambda_smooth(l):
    prob_count_arr = []
    print("++++++++", l)
    for x in range(0,len(occ_count_list),20):
        prob_count_arr.append([])

        for y in range(20):
            prob = (l + int(occ_count_list[x+y]))/(2*l + int(cat_count[y]))
            prob_count_arr[int(x/20)].append([prob,1-prob])

    return prob_count_arr
prob_arr = [lambda_smooth(0.01),lambda_smooth(0.1),lambda_smooth(0.2),lambda_smooth(0.5), lambda_smooth(1)]

#============================== CLASS COUNTER ==============================
import os
import re
ind_list = open('index_classify', 'r')
ind_all = ind_list.read()
ind_arr = ind_all.split()
ind_list.close()

ex_list = open('exception.txt', 'r')
ex_all = ex_list.read()
ex_arr = ex_all.split()
ex_list.close()

cat_dict = {'alt.atheism':0, 'comp.graphics':1, 'comp.os.ms-windows.misc':2,
'comp.sys.ibm.pc.hardware':3, 'comp.sys.mac.hardware':4, 'comp.windows.x':5,
'misc.forsale':6, 'rec.autos':7, 'rec.motorcycles':8, 'rec.sport.baseball':9,
'rec.sport.hockey':10, 'sci.crypt':11, 'sci.electronics':12, 'sci.med':13, 'sci.space':14,
'soc.religion.christian':15, 'talk.politics.guns':16, 'talk.politics.mideast':17,
'talk.politics.misc':18, 'talk.religion.misc':19}

cat_keys = list(cat_dict.keys())
cat_keys.sort()

dict_list = open('f-dictionary.txt', 'r')
dict_all = dict_list.read()
dict_arr = dict_all.split()
dict_list.close()

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

def bin_search(word, word_array):
    i = 0
    j = len(word_array) - 1
    while (j >= i):
        mid = int((i+j)/2)
        if (word_array[mid] == word):
            return mid
        if (max(word, word_array[mid]) == word):
            i = mid + 1
        else:
            j = mid - 1
    return False

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "classify/"
dir_path = os.path.join(script_dir, rel_path)

def readFile(filename):
    textfile = open(filename)
    text_all = textfile.read()
    textfile.close()
    splitter = re.split("[\s,]",text_all)
    text_arr = []
    for x in range(len(splitter)):
        word = pre_word(splitter[x])
        if (word != "" and bin_search(word, ex_arr) == False):
            text_arr.append(word)
    text_arr = list(set(text_arr))
    text_arr.sort()
    return text_arr

class_counter = []
for i in range(7539):
    class_counter.append([])

for count_f in range(11307, 18846):
    print(count_f)
    file_path = os.path.join(dir_path, str(count_f))
    text_arr = readFile(file_path)
    count = count_f - 11307
    for x in range(0,len(text_arr)):
        if (text_arr[x].isalpha()):
            d = bin_search(text_arr[x],dict_arr)
            if (d != False): #finds word in dict
                class_counter[count].append(d)
        elif (re.match(r'[a-z]+((\-|_)[a-z]+)+$', text_arr[x])):
            d = bin_search(text_arr[x],dict_arr)
            if (d != False): #finds word in dict
                class_counter[count].append(d)

        elif (re.match(r'[0-9]+--[0-9]+$', text_arr[x])):
            class_counter[count].append(14)

        elif (re.match(r'[0-9]+--[0-9]+$', text_arr[x])):
            class_counter[count].append(17)
            #_n--n_
        elif (re.match(r'[0-9]+-[0-9]+$', text_arr[x])):
            class_counter[count].append(20)
            #_n-n_
        elif (re.match(r'(([0-9]{4})|([0-9]{1,2}))-[0-9]{1,2}-(([0-9]{4})|([0-9]{1,2}))$', text_arr[x])):
            class_counter[count].append(5)
            #_date-_
        elif (re.match(r'[0-9]{3}-[0-9]{3}-[0-9]{4}$', text_arr[x])):
            class_counter[count].append(26)
            #_tel_
        elif (re.match(r'[0-9]{3}-[0-9]{2}-[0-9]{2}$', text_arr[x])):
            class_counter[count].append(26)
            #_tel_
        elif (re.match(r'[0-9]{3}-[0-9]{4}-[0-9]{2}$', text_arr[x])):
            class_counter[count].append(25)
            #_serial_
        elif (re.match(r'[0-9]+-[0-9]+-[0-9]+$', text_arr[x])):
            class_counter[count].append(19)
            #_n-n-n_
        elif (re.match(r'[0-1]-[0-9]+-[0-9]+-[0-9]$', text_arr[x])):
            class_counter[count].append(14)
            #_isbn_
        elif (re.match(r'1-[0-9]{3}-[0-9]{3}-[0-9]{4}$', text_arr[x])):
            class_counter[count].append(12)
            #_fax_
        elif (re.match(r'[0-9]+(-[0-9]+)+$', text_arr[x])):
            class_counter[count].append(18)
            #_n-n+_
        elif (re.search(r'mb/s$', text_arr[x])):
            class_counter[count].append(15)
            #_mb/s_
        elif (re.match(r'[0-9]+\.?[0-9]*\"x[0-9]', text_arr[x])):
            class_counter[count].append(7)
            #_dimen_
        elif (re.search(r'/each$', text_arr[x])):
            class_counter[count].append(9)
            #_each_
        elif (re.search(r'mph$', text_arr[x])):
            class_counter[count].append(16)
            #_mph_
        elif (re.match(r'[0-1]{8}b', text_arr[x])):
            class_counter[count].append(4)
            #_bin_
        elif (re.match(r'(([0][0-9])|([1][0-2]))(:[0-6][0-9]){1,2}(pm)?(am)?$', text_arr[x])):
            class_counter[count].append(27)
            #_time_
        elif (re.match(r'(([0-1][0-9])|([2][0-4]))(:[0-6][0-9]){1,2}(pm)?(am)?$', text_arr[x])):
            class_counter[count].append(27)
            #_time_
        elif (re.match(r'[0-9]+(:[0-9]+)+$', text_arr[x])):
            class_counter[count].append(22)
            #_n:n+_
        elif (re.match(r'[a-z0-9][^@]+@[a-z]+-?[a-z]+\.[a-z]+$', text_arr[x])):
            class_counter[count].append(10)
            #_email_
        elif (re.match(r'(([0-9]{4})|([0-9]{1,2}))/[0-9]{1,2}/(([0-9]{4})|([0-9]{1,2}))$', text_arr[x])):
            class_counter[count].append(6)
            #_date/_
        elif (re.match(r'[0-9]+(/[0-9]+)+$', text_arr[x])):
            class_counter[count].append(21)
            #_n/n+_
        elif (re.match(r'[0-9]+h$', text_arr[x])):
            class_counter[count].append(23)
            #_nh_
        elif (re.search(r'\"pne', text_arr[x])):
            class_counter[count].append(24)
            #_pne_
        elif (re.search(r'f9', text_arr[x])):
            class_counter[count].append(11)
            #_f9_
        elif (re.search(r'@\(\"', text_arr[x])):
            class_counter[count].append(1)
            #_@_
        elif (re.search(r'b8', text_arr[x])):
            class_counter[count].append(2)
            #_b8_
        elif (re.match(r'[x][a-z]+\(', text_arr[x])):
            class_counter[count].append(28)
            #_x(_
        elif (re.search(r'bhj',text_arr[x])):
            class_counter[count].append(3)
            #_bhj_
        elif (re.search(r'7e', text_arr[x])):
            class_counter[count].append(0)
            #_7e_
        elif (re.match(r'[a-z_\-]+(\.[a-z_\-]+)+$', text_arr[x])):
            class_counter[count].append(8)
            #_dots_
        elif (re.match(r'[a-z_\-]+\([a-z0-9_@&\-\$]+$', text_arr[x])):
            class_counter[count].append(13)
            #_func_

counter = open('file_dict.txt','w')
for x in range(len(class_counter)):
    counter.write(str(x+11307) + " = ")
    class_counter[x] = list(set(class_counter[x]))
    class_counter[x].sort()
    for y in range(len(class_counter[x])):
        counter.write(str(class_counter[x][y]) + " : " + dict_arr[class_counter[x][y]]+ " ")
    counter.write("\n")
counter.close()

#============================== MAXIMUM A POSTERIORI ==============================
def max_a_post(array, cat_ind, l):
    global cat_prob , dict_arr, prob_arr
    pcat = cat_prob[cat_ind]
    num = 1
    c = 0
    max_c = len(array)
    for x in range(len(dict_arr)):
        if (c < max_c):
            if (x == array[c]): #there exists
                num *= prob_arr[l][x][cat_ind][0]
                c += 1
            else:
                num *= prob_arr[l][x][cat_ind][1]
        else:
            num *= prob_arr[l][x][cat_ind][1]
    return num

def decide(array, l):
    arr_cat = []
    for x in range(20):
        arr_cat.append(max_a_post(array,x,l))
    max_cat = arr_cat[0]
    max_ind = 0
    for s in range(20):
        if (arr_cat[s] > max_cat):
            max_cat = arr_cat[s]
            max_ind = s
    return max_cat, cat_keys[max_ind]

l = 0.01
classification_name = "f_classify_" + str(l) + ".txt"
classification = open(classification_name, 'w')
for c in range(7539):
    print(l,c)
    prob_class, cat_class = decide(class_counter[c],0)
    classification.write(str(c+11307) + " " + cat_class + "\n")
classification.close()

l = 0.1
classification_name = "f_classify_" + str(l) + ".txt"
classification = open(classification_name, 'w')
for c in range(7539):
    print(l,c)
    prob_class, cat_class = decide(class_counter[c],1)
    classification.write(str(c+11307) + " " + cat_class + "\n")
classification.close()

l = 0.2
classification_name = "f_classify_" + str(l) + ".txt"
classification = open(classification_name, 'w')
for c in range(7539):
    print(l,c)
    prob_class, cat_class = decide(class_counter[c],2)
    classification.write(str(c+11307) + " " + cat_class + "\n")
classification.close()

l = 0.5
classification_name = "f_classify_" + str(l) + ".txt"
classification = open(classification_name, 'w')
for c in range(7539):
    print(l,c)
    prob_class, cat_class = decide(class_counter[c],3)
    classification.write(str(c+11307) + " " + cat_class + "\n")
classification.close()

l = 1
classification_name = "f_classify_" + str(l) + ".txt"
classification = open(classification_name, 'w')
for c in range(7539):
    print(l,c)
    prob_class, cat_class = decide(class_counter[c],4)
    classification.write(str(c+11307) + " " + cat_class + "\n")
classification.close()
